#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


try:
    with open('README.markdown', 'r') as readme:
        LONG_DESCRIPTION = readme.read()
except Exception:
    LONG_DESCRIPTION = None


setup(
    name='python-markdown-oembed',
    version='0.2.1',
    description="Markdown extension to allow media embedding using the oEmbed "
                "standard.",
    long_description=LONG_DESCRIPTION,
    author='Tanner Netterville',
    author_email='tannern@gmail.com',
    url='https://github.com/rennat/python-markdown-oembed',
    license='Public Domain',
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ),
    keywords='markdown oembed',

    packages=[
        'mdx_oembed',
    ],
    install_requires=[
        "python-oembed >= 0.2.1",
        "Markdown >= 2.6.1",
    ],

    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock'
    ]
)
