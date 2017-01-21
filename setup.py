from setuptools import setup

setup(
    name="electrum-lanacoin-server",
    version="1.0",
    scripts=['run_electrum_lanacoin_server.py','electrum-lanacoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumlanacoinserver':'src'
        },
    py_modules=[
        'electrumlanacoinserver.__init__',
        'electrumlanacoinserver.utils',
        'electrumlanacoinserver.storage',
        'electrumlanacoinserver.deserialize',
        'electrumlanacoinserver.networks',
        'electrumlanacoinserver.blockchain_processor',
        'electrumlanacoinserver.server_processor',
        'electrumlanacoinserver.processor',
        'electrumlanacoinserver.version',
        'electrumlanacoinserver.ircthread',
        'electrumlanacoinserver.stratum_tcp',
        'electrumlanacoinserver.stratum_http'
    ],
    description="lanacoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.deg",
    maintainer="lanacoin",
    maintainer_email="support@lanacoin.org",
    license="GNU Affero GPLv3",
    url="https://github.com/lanacoin/electrum-lanacoin-server/",
    long_description="""Server for the Electrum Lightweight lanacoin Wallet"""
)


