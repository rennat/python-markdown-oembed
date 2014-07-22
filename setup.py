#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


VERSION = '0.1.2'


setup(
    name='python-markdown-oembed',
    version=VERSION,
    description="Markdown extension to allow media embedding using the oEmbed "
                "standard.",
    author='Tanner Netterville',
    author_email='tannern@gmail.com',
    url='https://github.com/rennat/python-markdown-oembed',
    license='Public Domain',
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ),
    keywords='markdown oembed',

    packages=[
        'mdx_oembed',
    ],
    install_requires=[
        "python-oembed >= 0.2.1",
        "Markdown >= 2.2.0",
    ],

    test_suite='nose.collector',
    tests_require=['WebTest >= 1.2', 'BeautifulSoup', 'pytidylib', 'poster']
)
