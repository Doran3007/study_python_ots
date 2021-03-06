import asyncio
from aiohttp import ClientSession
from dataclasses import dataclass
from timeit import default_timer
from loguru import logger
from functools import wraps


#  декоратор для подсчета времени выполнения функции
def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        fun_res = func(*args, **kwargs)
        end_time = default_timer()
        print('Выполнение функции заняло: {:.4f}', end_time - start_time)
        return fun_res

    return wrapper


# Асинхронный декоратор подсчета времени выполнения
def time_decorator_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = default_timer()
        fun_res = await func(*args, **kwargs)
        end_time = default_timer()
        logger.info('Выполнение функции {} заняло: {:.4f}', args, end_time - start_time)
        return fun_res

    return wrapper


@dataclass
class Service:
    name: str
    url: str
    ip_field: str


SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]


async def fetch(session: ClientSession, url: str, ) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


@time_decorator_async
async def fetch_ip(service: Service) -> str:
    """
    :param service:
    :return:
    """
    # my_ip = "not found"
    async with ClientSession() as session:
        result = await fetch(session, service.url)

    logger.info("Результат для {}, результат {}", service.name, result)
    # my_ip = result[service.ip_field]
    return result[service.ip_field]


async def get_my_ip():
    done, pending = await asyncio.wait(
        [fetch_ip(s) for s in SERVICES],
        timeout=3,
        # return_when=asyncio.ALL_COMPLETED,
        return_when=asyncio.FIRST_COMPLETED,
    )
    for t in pending:
        logger.debug("Звершить функцию {}", t)
        t.cancel()

    my_ip = None
    for t in done:
        my_ip = t.result()
        break
    else:
        logger.warning("Нет результата!")

    logger.info("Получили мой ip! {}", my_ip)


def run_main():
    asyncio.run(get_my_ip())


if __name__ == '__main__':
    run_main()
