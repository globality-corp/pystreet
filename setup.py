#!/usr/bin/env python
from setuptools import find_packages, setup


project = "pystreet"
version = "1.0.0"

setup(
    name=project,
    version=version,
    description="Street address parsing and normalization",
    author="Globality Engineering",
    author_email="engineering@globality.com",
    url="https://github.com/globality-corp/pystreet",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "googlemaps>=2.5.1",
        "pyahocorasick>=1.1.6",
        "pycountry>=17.9.23",
        "unidecode>=1.0.22",
        "parameterized>=0.6.1",
    ],
    setup_requires=[
    ],
    tests_require=[
        "coverage>=3.7.1",
        "PyHamcrest>=1.9.0",
    ],
    extras_require={
        "test": [
            "aws-encryption-sdk>=2.0.0",
            "cryptography>=35",
            "coverage>=3.7.1",
            "PyHamcrest>=1.8.5",
            "pytest-cov>=3.0.0",
            "pytest>=6.2.5",
            "pytest-cov>=5.0.0",
        ],
        "lint": [
            "flake8",
            "flake8-print",
            "flake8-isort",
        ],
        "typehinting": [
            "mypy",
            "types-psycopg2",
            "types-python-dateutil",
            "types-pytz",
            "types-setuptools",
        ],
    },
)
