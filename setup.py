#!/usr/bin/env python
# -*- coding: ascii -*-

"""
A Monkey Patch for SleekXMPP 1.3.3 to allow for TLS Certificate
date validation for date prior to 2050


This software is licensed as described in the README.md and LICENSE
file, which you should have received as part of this distribution.

Changelog:
    - 2018-12-12 - Initial Commit
"""

import sys
import codecs
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

from sleekmonkey import __version__

VERSION          = __version__
DESCRIPTION      = 'Sleekmonkey is a not so elegant fix for the elegant SleekXMPP Python library.'
with codecs.open('README.md', 'r', encoding='UTF-8') as readme:
    LONG_DESCRIPTION = ''.join(readme)

CLASSIFIERS      = [ 'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                   ]

packages     = [ 'sleekmonkey']

setup(
    name             = "sleekmonkey",
    version          = VERSION,
    description      = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author       = 'Joe Porcelli',
    author_email = 'joe@kt3i.com',
    url          = 'http://github.com/porcej/sleekmonkey',
    license      = 'MIT',
    platforms    = [ 'any' ],
    packages     = packages,
    requires     = [ 'sleekxmpp' ],
    classifiers  = CLASSIFIERS
)
