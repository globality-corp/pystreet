#!/usr/bin/env python
from setuptools import find_packages, setup


project = "pystreet"
version = "0.3.0"

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
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    tests_require=[
        "coverage>=3.7.1",
        "parameterized>=0.6.1",
        "PyHamcrest>=1.9.0",
    ],
)
