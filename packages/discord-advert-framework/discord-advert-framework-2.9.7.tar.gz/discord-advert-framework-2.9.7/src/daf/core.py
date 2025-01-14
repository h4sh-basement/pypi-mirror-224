"""
    This module contains the essential definitions
    and functions needed for the framework to run,
    as well as user function to control the framework
"""
from typing import Callable, Coroutine, List, Optional, Union, overload
from pathlib import Path

from aiohttp import web as aiohttp_web
from typeguard import typechecked

from .logging.tracing import TraceLEVELS, trace
from .logging import _logging as logging, tracing

from . import guild
from . import client
from . import misc
from . import message
from . import convert
from . import remote

import asyncio
import shutil
import os
import sys
import pickle

import _discord as discord


__all__ = (
    "run",
    "shutdown",
    "add_object",
    "remove_object",
    "get_accounts",
    "initialize"
)


# -------------- CONSTANTS --------------
CORE_TASK_SLEEP_SEC = 0.1
ACCOUNT_CLEANUP_DELAY = 10
SCHEMA_BACKUP_DELAY = 120
DAF_PATH = Path.home().joinpath("daf")
SHILL_LIST_BACKUP_PATH = DAF_PATH.joinpath("objects.sbf")  # sbf -> Schema Backup File
# ---------------------------------------


class GLOBALS:
    """
    Storage class used for holding global variables.
    """
    accounts: List[client.ACCOUNT] = []
    tasks: List[asyncio.Task] = []
    running: bool = True
    save_to_file: bool = False
    remote_client: remote.RemoteAccessCLIENT = None

    cleanup_event = asyncio.Event()
    schema_backup_event = asyncio.Event()


# -----------------------------------------------------------------------
# HTTP tasks
# These must be in here due to needed interactions with core functions
# -----------------------------------------------------------------------
@remote.register("/accounts", "GET")
async def http_get_accounts():
    accounts = get_accounts()
    return remote.create_json_response(
        message=f"Retrieved {len(accounts)} accounts",
        accounts=convert.convert_object_to_semi_dict(accounts)
    )


@remote.register("/accounts", "POST")
async def http_add_account(account: dict):
    try:
        account = convert.convert_from_semi_dict(account)
        await add_object(account)
        return remote.create_json_response(message=f"Logged in to {account.client.user.display_name}")
    except Exception as exc:
        raise aiohttp_web.HTTPInternalServerError(reason=str(exc))


@remote.register("/accounts", "DELETE")
async def http_remove_account(account_id: int):
    account = misc.get_by_id(account_id)
    if account is None:
        raise aiohttp_web.HTTPInternalServerError(reason="Account not present")

    name = account.client.user.display_name
    await remove_object(account)
    return remote.create_json_response(message=f"Removed account {name}")


async def cleanup_accounts_task():
    """
    Task for cleaning up closed accounts.
    """
    loop = asyncio.get_event_loop()
    event = GLOBALS.cleanup_event
    while GLOBALS.running:
        loop.call_later(ACCOUNT_CLEANUP_DELAY, event.set)
        await event.wait()
        event.clear()
        for account in get_accounts():
            if account.deleted:
                await remove_object(account)


async def schema_backup_task():
    """
    Task for backing up the SCHEMA
    """
    loop = asyncio.get_event_loop()
    event = GLOBALS.schema_backup_event
    while GLOBALS.running:
        loop.call_later(SCHEMA_BACKUP_DELAY, event.set)
        await event.wait()
        event.clear()
        DAF_PATH.mkdir(parents=True, exist_ok=True)
        tmp_path = str(SHILL_LIST_BACKUP_PATH) + ".1"
        trace("Saving objects to file.", TraceLEVELS.DEBUG)
        try:
            with open(tmp_path, "wb") as writer:
                pickle.dump(convert.convert_object_to_semi_dict(GLOBALS.accounts), writer)

            shutil.copyfile(tmp_path, SHILL_LIST_BACKUP_PATH)
            os.remove(tmp_path)
        except Exception as exc:
            trace("Unable to save objects to file.", TraceLEVELS.ERROR, exc)


async def schema_load_from_file() -> None:
    """
    Restores the saved shilling list from file.
    """
    if not SHILL_LIST_BACKUP_PATH.exists():
        return

    trace("Restoring objects from file...", TraceLEVELS.NORMAL)
    with open(SHILL_LIST_BACKUP_PATH, "rb") as reader:
        accounts: List[client.ACCOUNT] = convert.convert_from_semi_dict(pickle.load(reader))

    trace("Updating accounts.", TraceLEVELS.DEBUG)
    for account in accounts:
        try:
            await account.update()  # Refresh without __init__ call
        except Exception as exc:
            trace(
                f"Unable to restore account {account}\n" +
                "Account still added to list to prevent data loss.\n" +
                "Use the GUI to edit / remove it.",
                TraceLEVELS.ERROR, exc
            )
        finally:
            # Save ID regardless if we failed result otherwise we cannot access though remote
            account._update_tracked_id()
            GLOBALS.accounts.append(account)

    trace(f"Restored objects from file ({len(GLOBALS.accounts)} accounts).", TraceLEVELS.NORMAL)


@misc.doc_category("DAF control reference")
async def initialize(user_callback: Optional[Union[Callable, Coroutine]] = None,
                     debug: Optional[Union[TraceLEVELS, int, str]] = TraceLEVELS.NORMAL,
                     logger: Optional[logging.LoggerBASE] = None,
                     accounts: List[client.ACCOUNT] = None,
                     save_to_file: bool = False,
                     remote_client: Optional[remote.RemoteAccessCLIENT] = None) -> None:
    """
    The main initialization function.
    It initializes all the other modules, creates advertising tasks
    and initializes all the core functionality.
    If you want to control your own event loop, use this instead of run.

    Parameters
    ---------------
    Any: Any
        Parameters are the same as in :func:`daf.core.run`.
    """
    loop = asyncio.get_event_loop()
    if accounts is None:
        accounts = []
    # ------------------------------------------------------------
    # Initialize tracing
    # ------------------------------------------------------------
    if debug is None:
        debug = TraceLEVELS.NORMAL

    tracing.initialize(debug)  # Print trace messages to the console for debugging purposes
    # ------------------------------------------------------------
    # Initialize logging
    # ------------------------------------------------------------
    if logger is None:
        logger = logging.LoggerJSON()

    await logging.initialize(logger)
    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # Initialize accounts
    # ------------------------------------------------------------
    # Load from file
    if save_to_file:
        try:
            await schema_load_from_file()
        except Exception as exc:
            trace("Unable to load from file", TraceLEVELS.ERROR, exc)

    for account in accounts:
        try:
            await add_object(account)
        except Exception as exc:
            trace("Unable to add account.", TraceLEVELS.ERROR, exc)

    # ------------------------------------------
    # Initialize remote access
    if remote_client is not None:
        await remote_client.initialize()
        remote.GLOBALS.remote_client = remote_client

    # ------------------------------------------
    # Create the user callback task
    if user_callback is not None:
        trace("Starting user callback function", TraceLEVELS.NORMAL)
        user_callback = user_callback()
        if isinstance(user_callback, Coroutine):
            GLOBALS.tasks.append(loop.create_task(user_callback))

    if save_to_file:  # Backup shilling list to pickle file
        GLOBALS.tasks.append(loop.create_task(schema_backup_task()))
    else:
        # Create account cleanup task (account self-deleted)
        # Only create if state preservation is disable to prevent potential data loss due to
        # lost connections or reset tokens. The user must use the GUI to cleanup any non-running accounts.
        GLOBALS.tasks.append(loop.create_task(cleanup_accounts_task()))

    GLOBALS.running = True
    GLOBALS.save_to_file = save_to_file
    trace("Initialization complete.", TraceLEVELS.NORMAL)


#######################################################################
# Functions
#######################################################################
@overload
@misc.doc_category("Dynamic mod.", True)
async def add_object(obj: client.ACCOUNT) -> None:
    """
    Adds an account to the framework.

    Parameters
    ------------
    obj: client.ACCOUNT
        The account object to add

    Raises
    ----------
    ValueError
        The account has already been added to the list.
    TypeError
        ``obj`` is of invalid type.
    """
    ...


@overload
@misc.doc_category("Dynamic mod.", True)
async def add_object(obj: Union[guild.USER, guild.GUILD, guild.AutoGUILD],
                     snowflake: client.ACCOUNT = None) -> None:
    """

    Adds a guild or an user to the daf.

    Parameters
    -----------
    obj: guild.USER | guild.GUILD | guild.AutoGUILD
        The guild object to add into the account (``snowflake``).
    snowflake: client.ACCOUNT=None
        The account to add this guild/user to.

    Raises
    ----------
    ValueError
        The guild/user is already added to the daf.
    TypeError
        The object provided is not supported for addition.
    TypeError
        Invalid parameter type.
    Other
        Raised in the obj.initialize() method
    """
    ...


@overload
@misc.doc_category("Dynamic mod.", True)
async def add_object(obj: Union[message.DirectMESSAGE, message.TextMESSAGE, message.VoiceMESSAGE],
                     snowflake: Union[guild.GUILD, guild.USER]) -> None:
    """
    Adds a message to the daf.

    Parameters
    -----------
    obj: message.DirectMESSAGE | message.TextMESSAGE | message.VoiceMESSAGE
        The message object to add into the daf.
    snowflake: guild.GUILD | guild.USER
        Which guild/user to add it to (can be snowflake id or a framework _BaseGUILD object or
        a discord API wrapper object).

    Raises
    ----------
    TypeError
        The object provided is not supported for addition.
    ValueError
        guild_id wasn't provided when adding a message object (to which guild should it add)
    ValueError
        Missing snowflake parameter.
    ValueError
        Could not find guild with that id.
    Other
        Raised in the obj.add_message() method
    """
    ...


async def add_object(obj, snowflake=None):
    object_type_name = type(obj).__name__

    # Add the object
    if isinstance(obj, client.ACCOUNT):
        if obj in GLOBALS.accounts:
            raise ValueError("Account already added to the list")

        await obj.initialize()
        GLOBALS.accounts.append(obj)
    elif isinstance(obj, (guild._BaseGUILD, guild.AutoGUILD)):
        if not isinstance(snowflake, client.ACCOUNT):
            raise TypeError("snowflake parameter type must be ACCOUNT when the obj parameter type is guild like.")

        await snowflake.add_server(obj)

    elif isinstance(obj, message.BaseMESSAGE):
        if snowflake is None:
            raise ValueError("snowflake parameter (guild-like) is required to add a message.")

        if not isinstance(snowflake, (guild.AutoGUILD, guild._BaseGUILD)):
            raise TypeError("snowflake parameter must be one of: guild.AutoGUILD, guild.GUILD, guild.USER")

        await snowflake.add_message(obj)

    else:
        raise TypeError(f"Invalid object type `{object_type_name}`.")


@typechecked
@misc.doc_category("Dynamic mod.")
async def remove_object(
    snowflake: Union[guild._BaseGUILD, message.BaseMESSAGE, guild.AutoGUILD, client.ACCOUNT]
) -> None:
    """
    .. versionchanged:: v2.4.1
        Turned async for fix bug of missing functionality

    .. versionchanged:: v2.4
        | Now accepts client.ACCOUNT.
        | Removed support for ``int`` and for API wrapper (PyCord) objects.

    Removes an object from the daf.

    Parameters
    -------------
    snowflake: guild._BaseGUILD | message.BaseMESSAGE | guild.AutoGUILD | client.ACCOUNT
        The object to remove from the framework.

    Raises
    --------------
    ValueError
        Item (with specified snowflake) not in the shilling list.
    TypeError
        Invalid argument."""
    if isinstance(snowflake, message.BaseMESSAGE):
        for account in GLOBALS.accounts:
            for guild_ in account.servers:
                if snowflake in guild_.messages:
                    guild_.remove_message(snowflake)
                    break
        else:
            raise ValueError("Message is not in any guilds")

    elif isinstance(snowflake, (guild._BaseGUILD, guild.AutoGUILD)):
        for account in GLOBALS.accounts:
            if snowflake in account.servers:
                account.remove_server(snowflake)

    elif isinstance(snowflake, client.ACCOUNT):
        await snowflake._close()
        GLOBALS.accounts.remove(snowflake)


@misc.doc_category("Clients")
def get_accounts() -> List[client.ACCOUNT]:
    """
    .. versionadded:: v2.4

    Returns
    ----------
    List[client.ACCOUNT]
        List of running accounts.
    """
    return GLOBALS.accounts.copy()


@typechecked
@misc.doc_category("DAF control reference")
async def shutdown() -> None:
    """
    Stops and cleans the framework.

    Parameters
    ----------
    loop: Optional[asyncio.AbstractEventLoop]
        The loop everything is running in.
        Leave empty for default loop.
        This parameter is only relevant if ``stop_loop`` is set to True.
    stop_loop: Optional[bool]
        Default: False; If True, it stops the running event loop.
    """
    trace("Shutting down...", TraceLEVELS.NORMAL)
    GLOBALS.running = False
    # Signal events for tasks to raise out of sleep
    GLOBALS.cleanup_event.set()
    GLOBALS.schema_backup_event.set()  # This also saves one last time, so manually saving is not needed
    # Close remote client
    if remote.GLOBALS.remote_client is not None:
        await remote.GLOBALS.remote_client._close()

    for task in GLOBALS.tasks:  # Wait for core tasks to finish
        await task

    GLOBALS.tasks.clear()
    for account in GLOBALS.accounts:
        await account._close()

    GLOBALS.accounts.clear()
    trace("Shutdown complete.", TraceLEVELS.NORMAL)


def _shutdown_clean(loop: asyncio.AbstractEventLoop) -> None:
    """
    Signals all accounts to cleanup and then close
    connections to Discord.

    Parameters
    ---------------
    loop: asyncio.AbstractEventLoop
        The loop to stop.
    """
    loop.run_until_complete(shutdown())


@typechecked
@misc.doc_category("DAF control reference")
def run(user_callback: Optional[Union[Callable, Coroutine]] = None,
        debug: Optional[Union[TraceLEVELS, int, str, bool]] = TraceLEVELS.NORMAL,
        logger: Optional[logging.LoggerBASE] = None,
        accounts: Optional[List[client.ACCOUNT]] = None,
        save_to_file: bool = False,
        remote_client: Optional[remote.RemoteAccessCLIENT] = None) -> None:
    """
    .. versionchanged:: 2.7

       Removed deprecated parameters (see :ref:`v2.7`)

    Runs the framework and does not return until the framework is stopped (:func:`daf.core.shutdown`).
    After stopping, it returns None.

    This will block until the framework is stopped, if you want manual control over the
    asyncio event loop, eg. you want to start the framework as a task, use
    the :func:`daf.core.initialize` coroutine.

    Parameters
    ---------------
    user_callback: Optional[Union[Callable, Coroutine]]
        Function or async function to call after the framework has been started.
    debug: Optional[TraceLEVELS | int | str] = TraceLEVELS.NORMAL
        .. versionchanged:: v2.3
            Deprecate use of bool (assume TraceLEVELS.NORMAL).
            Add support for TraceLEVELS or int or str that converts to TraceLEVELS.

        The level of trace for trace function to display.
        The higher value this option is, the more will be displayed.
    logger: Optional[loggers.LoggerBASE]
        The logging class to use.
        If this is not provided, JSON is automatically used with the ``path`` parameter set to /<user-home-dir>/daf/History
    accounts: Optional[List[client.ACCOUNT]]
        List of :class:`~daf.client.ACCOUNT` (Discord accounts) to use.
        .. versionadded:: v2.4
    save_to_file: Optional[bool]
        If ``True``, the shilling list (of accounts, guilds, messages, ...) will be saved to file
        and preserved on shutdown.

        It is recommended you set this to ``False`` when passing
        :func:`~daf.core.run` or :func:`~daf.core.initialize` the statically defined ``accounts`` parameter.

        .. note::

            Setting this to True and passing the ``accounts`` parameter as well, results in
            *Account already added* warnings.


    Raises
    ---------------
    ModuleNotFoundError
        Missing modules for the wanted functionality,
        install with ``pip install discord-advert-framework[optional-group]``.
    ValueError
        Invalid proxy url.
    """
    _params = locals().copy()

    if sys.version_info.minor < 10:
        loop = asyncio.get_event_loop()
    else:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    try:
        loop.create_task(initialize(**_params))
        loop.run_forever()
    except asyncio.CancelledError as exc:
        trace(exc, TraceLEVELS.ERROR)
    except KeyboardInterrupt:
        trace("Received a cancellation event. Stopping..", TraceLEVELS.WARNING)
    finally:
        _shutdown_clean(loop)
        asyncio.set_event_loop(None)
        loop.close()
