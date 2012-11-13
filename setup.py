#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


VERSION = '0.1'


setup(
    name='python-markdown-oembed',
    version=VERSION,
    description="",
    long_description=open('README.markdown').read(),
    author='Tanner Netterville',
    author_email='tannern@gmail.com',
    url='https://github.com/rennat/python-markdown-oembed',
    license='MIT',
    classifiers=(
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
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
