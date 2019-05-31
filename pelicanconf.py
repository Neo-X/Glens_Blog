#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Glen Berseth'
SITENAME = 'Glen Berseth'
SITEURL = ''
# SITEURL_ = 'www.fracturedplane.com'
# SITEURL_ = '/blog'
SITEURL_ = '/~gberseth/blog'

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
LINKS = (('Home', '/'),
         ('Publications', SITEURL_ + '/category/publication.html'),
         ('Projects', SITEURL_ + '/category/project.html'),
         ('Articles', SITEURL_ + '/category/article.html'),
         ('Links', SITEURL_ + '/links.php'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ["render_math"]


# DISQUS_SITENAME = "www-fracturedplane-com"
