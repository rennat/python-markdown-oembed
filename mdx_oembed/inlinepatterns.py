# -*- coding: utf-8 -*-
import logging
from markdown.inlinepatterns import Pattern


LOG = logging.getLogger(__name__)


OEMBED_LINK_RE = r'\!\[([^\]]*)\]\((https?://[^\)]*)' \
                 r'(?<!png)(?<!jpg)(?<!jpeg)(?<!gif)\)'


class OEmbedLinkPattern(Pattern):

    def __init__(self, pattern, markdown_instance=None, oembed_consumer=None):
        Pattern.__init__(self, pattern, markdown_instance)
        self.consumer = oembed_consumer

    def handleMatch(self, match):
        url = match.group(3).strip()
        response = self.consumer.embed(url)
        placeholder = self.markdown.htmlStash.store(response['html'])
        return placeholder
