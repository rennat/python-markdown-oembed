# -*- coding: utf-8 -*-
from mdx_oembed.extension import OEmbedExtension


def makeExtension(configs=None):
    return OEmbedExtension(configs=configs)
