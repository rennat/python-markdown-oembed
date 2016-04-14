# -*- coding: utf-8 -*-
import oembed

YOUTUBE = oembed.OEmbedEndpoint('http://www.youtube.com/oembed', [
    'https?://(*.)?youtube.com/*',
    'https?://youtu.be/*',
])

SLIDESHARE = oembed.OEmbedEndpoint('http://www.slideshare.net/api/oembed/2', [
    'http://www.slideshare.net/*/*',
    'http://fr.slideshare.net/*/*',
    'http://de.slideshare.net/*/*',
    'http://es.slideshare.net/*/*',
    'http://pt.slideshare.net/*/*',
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
    VIMEO,
    SLIDESHARE
]
