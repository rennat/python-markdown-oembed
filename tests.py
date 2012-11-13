# -*- coding: utf-8 -*-
import re
import unittest
import markdown
from mdx_oembed.extension import OEMBED_LINK_RE


class OEmbedPatternRegexTestCase(unittest.TestCase):
    def setUp(self):
        self.re = re.compile(OEMBED_LINK_RE)

    def test_ignore_relative_image_link(self):
        text = '![image](/image.png)'
        match = self.re.match(text)
        self.assertIsNone(match)

    def test_ignore_absolute_image_link(self):
        text = '![Mumbo Jumbo](http://tannern.com/mumbo-jumbo.jpg)'
        match = self.re.match(text)
        self.assertIsNone(match)

    def test_ignore_png_image_link(self):
        text = '![Mumbo Jumbo](http://tannern.com/mumbo-jumbo.png)'
        match = self.re.match(text)
        self.assertIsNone(match)

    def test_ignore_jpg_image_link(self):
        text = '![Mumbo Jumbo](http://tannern.com/mumbo-jumbo.jpg)'
        match = self.re.match(text)
        self.assertIsNone(match)

    def test_ignore_gif_image_link(self):
        text = '![Mumbo Jumbo](http://tannern.com/mumbo-jumbo.gif)'
        match = self.re.match(text)
        self.assertIsNone(match)

    def test_find_youtube_link(self):
        text = '![video](http://www.youtube.com/watch?v=zqnh_YJBvOI)'
        match = self.re.match(text)
        self.assertIsNotNone(match)

    def test_find_youtube_short_link(self):
        text = '![video](http://youtu.be/zqnh_YJBvOI)'
        match = self.re.match(text)
        self.assertIsNotNone(match)


class OEmbedExtensionTestCase(unittest.TestCase):
    def setUp(self):
        self.markdown = markdown.Markdown(extensions=['oembed'])


class IgnoredTestCase(OEmbedExtensionTestCase):
    """
    The OEmbedExtension should ignore these tags allowing markdown's image
    processor to find and handle them.
    """

    def test_relative(self):
        text = '![alt](image.png)'
        expected = '<p><img alt="alt" src="image.png" /></p>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

    def test_slash_relative(self):
        text = '![alt](/image.png)'
        expected = '<p><img alt="alt" src="/image.png" /></p>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

    def test_absolute(self):
        text = '![Mumbo Jumbo](http://tannern.com/mumbo-jumbo.jpg)'
        expected = '<p><img alt="Mumbo Jumbo" src="http://tannern.com/mumbo-jumbo.jpg" /></p>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)


class YoutubeTestCase(OEmbedExtensionTestCase):
    """
    The OEmbedExtension should handle embedding for these cases.
    """

    def test_youtube_link(self):
        """
        YouTube video link.
        """
        text = '![video](http://www.youtube.com/watch?v=zqnh_YJBvOI)'
        expected = '<iframe width="459" height="344" src="http://www.youtube.com/embed/zqnh_YJBvOI?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

    def test_youtube_short_link(self):
        """
        Short format YouTube video link.
        """
        text = '![video](http://youtu.be/zqnh_YJBvOI)'
        expected = '<iframe width="459" height="344" src="http://www.youtube.com/embed/zqnh_YJBvOI?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

    def test_vimeio_link(self):
        """
        Vimeo video link.
        """
        text = '![link](http://vimeo.com/52970271)'
        expected = '<iframe src="http://player.vimeo.com/video/52970271" width="1280" height="720" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)


class LimitedOEmbedExtensionTestCase(unittest.TestCase):
    def setUp(self):
        self.markdown = markdown.Markdown(
            extensions=['oembed'],
            extension_configs={
                'oembed': {
                    'allowed_endpoints': ['youtube',],
                }
            })

    def test_youtube_link(self):
        """
        YouTube video link.
        """
        text = '![video](http://www.youtube.com/watch?v=zqnh_YJBvOI)'
        expected = '<iframe width="459" height="344" src="http://www.youtube.com/embed/zqnh_YJBvOI?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

    def test_youtube_short_link(self):
        """
        Short format YouTube video link.
        """
        text = '![video](http://youtu.be/zqnh_YJBvOI)'
        expected = '<iframe width="459" height="344" src="http://www.youtube.com/embed/zqnh_YJBvOI?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

    def test_vimeio_link(self):
        """
        Vimeo video link.
        """
        text = '![link](http://vimeo.com/52970271)'
        expected = '<p><img alt="link" src="http://vimeo.com/52970271" /></p>'
        output = self.markdown.convert(text)
        self.assertEqual(output, expected)

