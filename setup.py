from setuptools import setup, find_packages

LOCAWEB_GATEWAY_VERSION = 'v0.1.1'

setup(name='locaweb_gateway',
    version=LOCAWEB_GATEWAY_VERSION,
    description='',
    author='locaweb',
    packages=['locaweb_gateway'],
    install_requires=['requests >= 0.8.8', 'simplejson'],
    author_email = "saas-dev@locaweb.com.br",
    license = "MIT license",
    keywords = "locaweb gateway pagamento checkout",
    url = "https://github.com/locaweb/locaweb-gateway-python",
    include_package_data=True
)
