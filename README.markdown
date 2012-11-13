# Python Markdown oEmbed

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
