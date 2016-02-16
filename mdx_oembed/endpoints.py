# -*- coding: utf-8 -*-
import oembed


DEFAULT_ENDPOINTS = [
    # Youtube
    oembed.OEmbedEndpoint('http://www.youtube.com/oembed', [
        'https?://(*.)?youtube.com/*',
        'https?://youtu.be/*',
    ]),

    # Flickr
    oembed.OEmbedEndpoint('http://www.flickr.com/services/oembed/', [
        'https?://*.flickr.com/*',
    ]),

    # Vimeo
    oembed.OEmbedEndpoint('http://vimeo.com/api/oembed.json', [
        'https?://vimeo.com/*',
    ]),
]
