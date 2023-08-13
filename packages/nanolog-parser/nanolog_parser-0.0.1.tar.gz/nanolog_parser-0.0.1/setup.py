from setuptools import setup, find_packages

setup(
    name="nanolog_parser",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nanologp=nanolog_parser.parse:main',
        ],
    },
)
