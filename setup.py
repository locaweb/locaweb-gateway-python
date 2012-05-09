from distutils.core import setup

LOCAWEB_GATEWAY_VERSION = 'v0.0.1'

setup(
    name='locaweb_gateway',
    version=LOCAWEB_GATEWAY_VERSION,
    description='Locaweb gateway bindings',
    author='Locaweb',
    packages=[],
    install_requires=['requests >= 0.8.8', 'simplejson']
)
