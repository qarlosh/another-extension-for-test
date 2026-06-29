from importlib import metadata
import os
import platform
import sys

from connect.eaas.core.decorators import router, web_app
from connect.eaas.core.extension import WebApplicationBase


def _package_version(name):
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return None


@web_app(router)
class AnotherExtensionForTestWebApplication(WebApplicationBase):

    @router.get('/environment_info', summary='Runtime environment info')
    async def environment_info(self):
        return {
            'python_version': platform.python_version(),
            'python_full_version': sys.version,
            'python_executable': sys.executable,
            'platform': platform.platform(),
            'environment': dict(os.environ),
            'connect_eaas_core': _package_version('connect-eaas-core'),
            'connect_extension_runner': _package_version('connect-extension-runner'),
            'packages': dict(sorted(
                (dist.metadata['Name'], dist.version)
                for dist in metadata.distributions()
                if dist.metadata['Name']
            )),
        }
