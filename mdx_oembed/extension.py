# -*- coding: utf-8 -*-
from markdown import Extension
import oembed
from mdx_oembed.endpoints import ENDPOINTS
from mdx_oembed.inlinepatterns import OEmbedLinkPattern, OEMBED_LINK_RE


class OEmbedExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        self.oembed_consumer = self.prepare_oembed_consumer()
        pattern = OEmbedLinkPattern(OEMBED_LINK_RE, md, self.oembed_consumer)
        md.inlinePatterns.add('oembed_link', pattern, '<image_link')

    def prepare_oembed_consumer(self):
        allowed_endpoints = self.getConfig('allowed_endpoints',
                                           ENDPOINTS.keys())
        consumer = oembed.OEmbedConsumer()
        [consumer.addEndpoint(v)
         for k,v in ENDPOINTS.items()
         if k in allowed_endpoints]
        return consumer
