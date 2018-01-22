#!/usr/bin/env python
from setuptools import find_packages, setup


project = "pystreet"
version = "0.1.0"

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
        "pyparsing>=2.1.8",
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
