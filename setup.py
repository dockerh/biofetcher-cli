from setuptools import setup, find_packages

setup(
    name='biofetcher',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'aiohttp',
        'aiofiles'
    ],
    entry_points={
        'console_scripts': [
            'biofetcher=biofetcher.cli:main',
        ],
    },
)
