# -*- coding: utf-8 -*-
import oembed

YOUTUBE = oembed.OEmbedEndpoint('http://www.youtube.com/oembed', [
    'https?://(*.)?youtube.com/*',
    'https?://youtu.be/*',
])

FLICKR = oembed.OEmbedEndpoint('http://www.flickr.com/services/oembed/', [
    'https?://*.flickr.com/*',
])

VIMEO = oembed.OEmbedEndpoint('http://vimeo.com/api/oembed.json', [
    'https?://vimeo.com/*',
])

DEFAULT_ENDPOINTS = [
    YOUTUBE,
    FLICKR,
    VIMEO
]
