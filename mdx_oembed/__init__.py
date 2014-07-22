# -*- coding: utf-8 -*-
from mdx_oembed.extension import OEmbedExtension


VERSION = '0.1.3'


def makeExtension(configs=None):
    if isinstance(configs, list):
        configs = dict(configs)
    return OEmbedExtension(configs=configs)
