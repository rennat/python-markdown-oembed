# Python Markdown oEmbed

[![Build Status](https://travis-ci.org/rennat/python-markdown-oembed.svg?branch=master)](https://travis-ci.org/rennat/python-markdown-oembed)

Markdown extension to allow media embedding using the oEmbed standard.

## Installation

    pip install python-markdown-oembed

## Usage

    >>> import markdown
    >>> md = markdown.Markdown(extensions=['oembed'])
    >>> md.convert('![video](http://www.youtube.com/watch?v=zqnh_YJBvOI)')
    u'<iframe width="459" height="344" src="http://www.youtube.com/embed/zqnh_YJBvOI?fs=1&feature=oembed" frameborder="0" allowfullscreen></iframe>'

## Links

- [python-markdown-oembed](https://github.com/rennat/python-markdown-oembed)
- [Markdown](http://daringfireball.net/projects/markdown/)
- [oEmbed](http://www.oembed.com/)
- [python-oembed](https://github.com/abarmat/python-oembed)

## License

A Public Domain work. Do as you wish.

## Changelog

### 0.2.1

- add Slideshare endpoint (thanks to [anantshri](https://github.com/anantshri))

### 0.2.0

- backwards incompatible changes
    - allows arbitrary endpoints ([commit](https://github.com/Wenzil/python-markdown-oembed/commit/1e89de9db5e63677e071c36503e2499bbe0792da))
    - works with modern Markdown (>=2.6)
    - dropped support for python 2.6
- added support python 3.x
