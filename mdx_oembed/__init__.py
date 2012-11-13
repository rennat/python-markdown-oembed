# -*- coding: utf-8 -*-
from mdx_oembed.extension import OEmbedExtension


def makeExtension(configs=None):
    if isinstance(configs, list):
        configs = dict(configs)
    return OEmbedExtension(configs=configs)
