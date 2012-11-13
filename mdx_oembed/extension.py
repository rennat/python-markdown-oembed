# -*- coding: utf-8 -*-
from markdown import Extension
import oembed
from mdx_oembed.endpoints import ENDPOINTS
from mdx_oembed.inlinepatterns import OEmbedLinkPattern, OEMBED_LINK_RE


AVAILABLE_ENDPOINTS = ENDPOINTS.keys()


class OEmbedExtension(Extension):

    config = {
        'allowed_endpoints': [
            AVAILABLE_ENDPOINTS,
            "A list of oEmbed endpoints to allow. Possible values are "
            "{}.".format(', '.join(AVAILABLE_ENDPOINTS)),
        ],
    }

    def extendMarkdown(self, md, md_globals):
        self.oembed_consumer = self.prepare_oembed_consumer()
        link_pattern = OEmbedLinkPattern(OEMBED_LINK_RE, md,
                                         self.oembed_consumer)
        md.inlinePatterns.add('oembed_link', link_pattern, '<image_link')

    def prepare_oembed_consumer(self):
        allowed_endpoints = self.getConfig('allowed_endpoints',
                                           AVAILABLE_ENDPOINTS)
        consumer = oembed.OEmbedConsumer()
        [consumer.addEndpoint(v)
         for k,v in ENDPOINTS.items()
         if k in allowed_endpoints]
        return consumer
