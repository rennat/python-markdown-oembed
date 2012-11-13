# -*- coding: utf-8 -*-
import oembed


ENDPOINTS = {
    'youtube': oembed.OEmbedEndpoint('http://www.youtube.com/oembed', [
        'http://(*.)?youtube.com/*',
        'http://youtu.be/*',
    ]),
    'flickr': oembed.OEmbedEndpoint('http://www.flickr.com/services/oembed/', [
        'http://*.flickr.com/*',
    ]),
    'vimeo': oembed.OEmbedEndpoint('http://vimeo.com/api/oembed.json', [
        'http://vimeo.com/*',
    ]),
}
