#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('cmdline_sharepoint/cmdline_sharepoint.py').read(),
    re.M
    ).group(1)

setup(
    name = "cmdline-sharepoint",
    packages=find_packages(),
    package_data={
        "": ["SAML.xml"]
    },
    entry_points = {
        "console_scripts": ['cmdline_sharepoint = cmdline_sharepoint.__main__:main']
        },
    version = version,
    description="SharePoint REST client for Python",
    author="Nicolae Rogojan",
    author_email="rogojan.colea@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries"
    ],
    install_requires=['requests'],
    )
