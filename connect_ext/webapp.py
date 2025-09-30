from starlette.responses import PlainTextResponse
from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.decorators import router, web_app


@web_app(router)
class AnotherExtensionForTestWebApplication(WebApplicationBase):
    @router.get('/test_endpoint', summary='Some test endpoint')
    async def test_endpoint(self):
        return PlainTextResponse(
            status_code=200,
            content="response from test endpoint",
        )
