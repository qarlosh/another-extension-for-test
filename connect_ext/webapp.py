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


@web_app(router)
class AnotherExtensionForTestWebApplication(WebApplicationBase):

    @router.post('/alloc_mem', summary='Alloc mem', response_model=AllocMemResponse)
    async def alloc_mem(self, request: AllocMemRequest, logger: LoggerAdapter = Depends(get_logger)):
        return alloc_mem(logger, request)

    @router.post('/clear_mem', summary='Clear mem', response_model=ClearMemResponse)
    async def clear_mem(self, logger: LoggerAdapter = Depends(get_logger)):
        return clear_mem(logger)
