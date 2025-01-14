import asyncio
import logging
from asyncio import TimeoutError
from typing import Callable, TypeVar

log = logging.getLogger("Timeout")

T = TypeVar("T")


def timeout(func: Callable[..., T], *, secs: int = 0) -> T | None:
    """
    Sets a timeout for a given lambda function
    :param func: The callable function
    :param secs: The timeout in seconds
    """

    async def main_supervisor(func: Callable[..., T], secs: int) -> T:
        runner = asyncio.to_thread(func)
        task = asyncio.create_task(runner)
        if secs == 0:
            return await task
        else:
            return await asyncio.wait_for(task, timeout=secs)

    loop = asyncio.get_event_loop()
    try:
        complete = loop.run_until_complete(main_supervisor(func, secs))
        return complete
    except TimeoutError:
        log.error(
            f"Kafka Connect operation {func.__name__} timed out after {secs} seconds. To increase the duration, set the `timeout` option in config.yaml."
        )
