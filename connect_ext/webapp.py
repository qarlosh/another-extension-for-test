import psutil
import asyncio
from logging import LoggerAdapter
from fastapi import Depends
from connect_ext.memdiag import (
    alloc_mem,
    clear_mem,
    AllocMemRequest,
    AllocMemResponse,
    ClearMemResponse,
)
from starlette.responses import PlainTextResponse
from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.decorators import router, web_app
from connect.eaas.core.inject.common import get_logger

async_tasks = set()


async def counter(logger):
    c = 0
    while True:
        await asyncio.sleep(5)
        c += 5
        logger.info(f"Counter: {c} sec")


def _mb(n):
    return int(n / (1024 * 1024) )


async def memory_monitor(logger):
    while True:
        await asyncio.sleep(5)
        mem = psutil.virtual_memory()
        logger.info(f"TOTL: {_mb(mem.total)} AVLBL: {_mb(mem.available)} [{mem.percent} %] USED: {_mb(mem.used)} FREE: {_mb(mem.free)} ACTIV: {_mb(mem.active)}")


@web_app(router)
class AnotherExtensionForTestWebApplication(WebApplicationBase):

    @router.post('/alloc_mem', summary='Alloc mem', response_model=AllocMemResponse)
    async def alloc_mem(self, request: AllocMemRequest, logger: LoggerAdapter = Depends(get_logger)):
        return alloc_mem(logger, request)

    @router.post('/clear_mem', summary='Clear mem', response_model=ClearMemResponse)
    async def clear_mem(self, logger: LoggerAdapter = Depends(get_logger)):
        return clear_mem(logger)

    @router.post('/start_counter_task', summary='Start counter task')
    async def start_counter_task(self, logger: LoggerAdapter = Depends(get_logger)):
        task = asyncio.create_task(counter(logger))
        async_tasks.add(task)
        return PlainTextResponse('Counter task started', status_code=200)

    @router.post('/start_memory_monitor', summary='Start memory monitor')
    async def start_memory_monitor(self, logger: LoggerAdapter = Depends(get_logger)):
        task = asyncio.create_task(memory_monitor(logger))
        async_tasks.add(task)
        return PlainTextResponse('Memory monitor started', status_code=200)
