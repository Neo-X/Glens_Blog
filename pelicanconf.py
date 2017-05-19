#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Glen'
SITENAME = 'Glens Blog'
SITEURL = 'localhost/blog/'

PATH = 'content'

TIMEZONE = 'Canada/Pacific'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', 'http://www.fracturedplane.com'),
         ('Publications', 'http://www.fracturedplane.com/blog/category/publication.html'),
         ('Projects', 'http://www.fracturedplane.com/blog/category/project.html'),
         ('Links', 'http://www.fracturedplane.com/links.php'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'
