# -*- coding: utf-8 -*-
from markdown import Extension
import oembed
from mdx_oembed.endpoints import DEFAULT_ENDPOINTS
from mdx_oembed.inlinepatterns import OEmbedLinkPattern, OEMBED_LINK_RE


class OEmbedExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'allowed_endpoints': [
                DEFAULT_ENDPOINTS,
                "A list of oEmbed endpoints to allow. Defaults to "
                "endpoints.DEFAULT_ENDPOINTS"
            ],
        }
        super(OEmbedExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        self.oembed_consumer = self.prepare_oembed_consumer()
        link_pattern = OEmbedLinkPattern(OEMBED_LINK_RE, md,
                                         self.oembed_consumer)
        md.inlinePatterns.add('oembed_link', link_pattern, '<image_link')

    def prepare_oembed_consumer(self):
        allowed_endpoints = self.getConfig('allowed_endpoints', DEFAULT_ENDPOINTS)
        consumer = oembed.OEmbedConsumer()

        if allowed_endpoints:
            for endpoint in allowed_endpoints:
                consumer.addEndpoint(endpoint)

        return consumer
