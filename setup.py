#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
   from distutils.command.build_py import build_py_2to3 \
        as build_py
except ImportError:
    from distutils.command.build_py import build_py

from setuptools import setup
#from distutils.core import setup
import restshlib

setup(
    name = 'restsh',
    version = ":versiontools:restshlib:",
    description = "A simple rest shell client",
    long_description = "",
    keywords = 'rest shell',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/jespino/restsh',
    license = 'BSD',
    include_package_data = True,
    packages = ['restshlib', ],
    scripts = ['restsh', ],
    install_requires=[
        'requests',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    cmdclass = {'build_py': build_py},
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ]
)
