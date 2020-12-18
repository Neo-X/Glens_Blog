#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Glen Berseth'
SITENAME = 'Glen Berseth'
# SITEURL = 'http://www.fracturedplane.com'
SITEURL = ''
SITEURL_ = 'http://www.fracturedplane.com'
# SITEURL_ = '/blog'
SITEURL_ = ''
# SITEURL_ = ''

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
         ('Papers', SITEURL_ + '/category/publication.html'),
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



DESCRIPTION = """I received my PhD at the Department of Computer Science at the University of British Columbia in 2019 where I worked on reinforcement learning, machine learning and motion planning with <a href="https://www.cs.ubc.ca/~van/">Michiel van de Panne</a>. I received my BSc degree in Computer Science from York University in 2012 and my MSc from York University under the supervision of <a href="www.cse.yorku.ca/~pfal/">Petros Faloutsos</a> in 2014 for optimization and authoring crowd simulations. I have published in a wide range of areas including computer animation, machine learning and robotics and am a NSERC scholarship award winner. You can find a list of projects and publications <a href="./category/publication.html">here</a>.
 </br>
 </br>
 The goal of my research is to develop systems that can learn and act in the world intelligently. Much of my work has focused on combining deep learning and reinforcement learning methods to solve complex, high-dimensional perception and planning problems. In general, my research builds on data-driven methods with interdisciplinary impacts across manufacturing, automation, medical applications, computer simulations and education."""

SITESUBTITLE = """I am a Postdoctoral Researcher at the <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>. My research combines deep learning and reinforcement learning on high-dimensional control problems."""

NEWS = (
         'Aug 2020: Deep Integration of Physical Humanoid Control and Crowd Navigation <span style="font-weight:bold;">receives best paper runner up at MIG2020</span>',
         'Sep 2019: Visual Imitation work featured in MIT CSAIL podcast',
         'Apr 2019: Started PostDoc at <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> group working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning Lab (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>',
         'Feb 2019: Defended Ph.D. Thesis at the University of British Columbia under the supervision of <a href="https://www.cs.ubc.ca/~van/">Michiel van de Panne</a> ',
         'Aug 2017: SIGGRAPH paper DeepLoco: Dynamic Locomotion Skills Using Hierarchical Deep Reinforcement Learning covered in the <a href="https://www.popularmechanics.com/technology/news/a27581/deeploco-deep-learning-run-bot-siggraph-2017/">Popular Mechanics</a>.',
         'Mar 2017: Awarded NSERC PhD scholarship',
         'Mar 2016: Robust Space-Time Footsteps for Agent-Based Steering receives <span style="font-weight:bold;">best short paper award</span> as CASA 2016',
         )

RESEARCHAREAS= ("HeirarchicalRL", "UnsupervisedRL", "Multi-Task")
# DISQUS_SITENAME = "www-fracturedplane-com"
