"""Get statuses from Minecraft servers"""
import asyncio
from mcstatus.address import (
    Address,
    async_minecraft_srv_address_lookup,
    minecraft_srv_address_lookup,
)
from mcstatus.pinger import AsyncServerPinger, ServerPinger
from mcstatus.protocol.connection import (
    Connection,
    TCPAsyncSocketConnection,
    TCPSocketConnection,
)

try:
    import orjson as json
    from orjson import JSONDecodeError
except:
    import json
    from json import JSONDecodeError

from .exceptions import InvalidResponseError, ServerTimeoutError

__version__ = "0.3.0"

### Code used for both async and sync ###


def _request_status(conn: Connection):
    """Send a status request packet to the server

    Args:
        conn (Connection): The connection to send the request with
    """
    request = Connection()
    request.write_varint(0)
    conn.write_buffer(request)


def _parse_status(response: Connection) -> dict:
    """Parse the status response from a server

    Args:
        response (Connection): The server response

    Raises:
        InvalidResponseError: If the server gave an invalid response

    Returns:
        dict: The parsed status response
    """
    if response.read_varint() != 0:
        raise InvalidResponseError("Invalid status response packet from server")

    try:
        status = json.loads(response.read_utf())
        if not isinstance(status, dict):
            raise InvalidResponseError("Status response was not a dictionary")

        return status
    except (JSONDecodeError, UnicodeDecodeError) as e:
        raise InvalidResponseError("Failed to decode status response", e)


### Async API ###


class AsyncPinger(AsyncServerPinger):
    """An async server pinger that returns the parsed status reponse without modification"""

    async def read_status(self):
        _request_status(self.connection)
        response = await self.connection.read_buffer()
        return _parse_status(response)


async def async_status(
    ip: str,
    port: int = 25565,
    timeout: float = 5,
    *,
    srv_check=True,
):
    """Async function to get a server's status

    Args:
        ip (str): The server's IP
        port (int, optional): The server's port. Defaults to 25565.
        timeout (float, optional): The time to wait for the server to respond. Defaults to 5.
        srv_check (bool, optional): Whether to check the SRV record of the server. Defaults to True.

    Raises:
        TimeoutError: If the server took too long to respond
        InvalidResponseError: If the server gave an invalid response

    Returns:
        dict: The parsed status response
    """
    if srv_check:
        addr = await async_minecraft_srv_address_lookup(
            f"{ip}:{port}",
            default_port=port,
            lifetime=timeout,
        )
    else:
        addr = Address(ip, port)

    try:
        connection = TCPAsyncSocketConnection(addr, timeout)
        await connection.connect()

        pinger = AsyncPinger(connection, addr)
        pinger.handshake()
        return await pinger.read_status()
    except asyncio.exceptions.TimeoutError as e:
        raise ServerTimeoutError(
            f"Server did not respond in the provided amount of time ({ip}:{port})", e
        )
    except (IndexError, IOError) as e:
        raise InvalidResponseError(f"Server did not respond properly ({ip}:{port})", e)


### Sync API ###


class Pinger(ServerPinger):
    """A server pinger that returns the parsed status reponse without modification"""

    def read_status(self):
        _request_status(self.connection)
        response = self.connection.read_buffer()
        return _parse_status(response)


def status(
    ip: str,
    port: int = 25565,
    timeout: float = 5,
    *,
    srv_check=True,
):
    """Function to get a server's status

    Args:
        ip (str): The server's IP
        port (int, optional): The server's port. Defaults to 25565.
        timeout (float, optional): The time to wait for the server to respond. Defaults to 5.
        srv_check (bool, optional): Whether to check the SRV record of the server. Defaults to True.

    Raises:
        TimeoutError: If the server took too long to respond
        InvalidResponseError: If the server gave an invalid response

    Returns:
        dict: The parsed status response
    """
    if srv_check:
        addr = minecraft_srv_address_lookup(
            f"{ip}:{port}",
            default_port=port,
            lifetime=timeout,
        )
    else:
        addr = Address(ip, port)

    try:
        connection = TCPSocketConnection(addr, timeout)

        pinger = Pinger(connection, addr)
        pinger.handshake()
        return pinger.read_status()
    except asyncio.exceptions.TimeoutError as e:
        raise ServerTimeoutError(
            f"Server did not respond in the provided amount of time ({ip}:{port})", e
        )
    except (IndexError, IOError) as e:
        raise InvalidResponseError(f"Server did not respond properly ({ip}:{port})", e)
