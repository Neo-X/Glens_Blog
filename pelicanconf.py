#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Glen Berseth'
SITENAME = 'Glen Berseth'
SITEURL = ''
# SITEURL_ = 'www.fracturedplane.com'
# SITEURL_ = '/blog'
SITEURL_ = '~gberseth'
SITEURL_ = ''

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
         ('Links', SITEURL_ + '/links.html'),
         ('Info', SITEURL_ + '/info.html'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'
# THEME = 'themes/blue-penguin'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ["render_math"]


SITESUBTITLE = 'I am a PostDoctoral Researcher at the <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> group working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning Lab (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>.'

DESCRIPTION = 'I am a PostDoctoral Researcher at the <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> group working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning Lab (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>. I received my PhD at the Department of Computer Science at the University of British Columbia in 2019 where I worked on reinforcement learning, machine learning and motion planning with <a href="https://www.cs.ubc.ca/~van/">Michiel van de Panne</a>. I received my BSc degree in Computer Science from York University in 2012 and my MSc from York University under the supervision of <a href="www.cse.yorku.ca/~pfal/">Petros Faloutsos</a> in 2014 for optimization and authoring crowd simulations. I have published in a wide range of areas including computer animation, machine learning and robotics and am a NSERC scholarship award winner. You can find a list of projects and publications <a href="./category/publication.html">here</a>.'


# DISQUS_SITENAME = "www-fracturedplane-com"
