# -*- coding: utf-8 -*-
from mdx_oembed.extension import OEmbedExtension


VERSION = '0.1.7'


def makeExtension(**kwargs):
    return OEmbedExtension(**kwargs)
