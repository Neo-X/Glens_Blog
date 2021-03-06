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
LINKS = (
         ('Papers', SITEURL_ + '/category/publication.html'),
         ('Google Scholar', 'https://scholar.google.ca/citations?user=-WZcuuwAAAAJ&hl=en'),
         ('twitter', "https://twitter.com/GlenBerseth"),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 500

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'
# THEME = 'themes/blue-penguin'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ["render_math"]


#  </br> 
#  While learning agents hold the promise of being general problem-solvers, they often struggle with environmental and task diversity.
#  My work aims to move away from training agents to maximize reward on narrow tasks and instead looks into developing agents that learn general-purpose skills that contribute to solving a wide variety of tasks.
#  Specifically, my work has focused on combining deep learning and reinforcement learning methods to solve high-dimensional perception and planning problems.
#  </br> 
DESCRIPTION = """
    I received my PhD at the Department of Computer Science at the University of British Columbia in 2019 where I worked on reinforcement learning, machine learning and motion planning with <a href="https://www.cs.ubc.ca/~van/">Michiel van de Panne</a>.
    I received my BSc degree in Computer Science from York University in 2012 and my MSc from York University under the supervision of <a href="www.cse.yorku.ca/~pfal/">Petros Faloutsos</a> in 2014 for optimization and authoring crowd simulations. I have published in a wide range of areas including computer animation, machine learning and robotics and am a NSERC scholarship award winner.
    I have also worked at IBM (2012) and with <a href="https://mila.quebec/en/person/pal-christopher/">Christopher Pal</a> at ElementAI (2018). 
    You can find a list of projects and publications <a href="./category/publication.html">here</a>.
 </br>
 </br> 
 Interested in joining my group?
 <ul>
 
    <li>Students interested in an undergraduate research position please apply through <a href="https://docs.google.com/forms/d/e/1FAIpQLSfx8MJ1e72tB9UuzjeIJb0CX5k43ASwimhx63sWzZnEyc4dtA/viewform?usp=sf_link">this form</a>.</li>
    <li>Students interest in a MSc/PhD please apply through <a href="https://mila.quebec/en/cours/supervision/">Mila admissions</a>.</li>
    <li>Students interest in a Postdoctoral position please apply through <a href="https://docs.google.com/forms/d/e/1FAIpQLScDW9mQ0pNqeDix8Nsrt8uFOMxNTmBmxyszed-R9cX5lkZ5ag/viewform?usp=sf_link">this form</a>.</li>
</ul>
"""

SITESUBTITLE = """I am a Postdoctoral Researcher at the <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>. My research combines deep learning and reinforcement learning on high-dimensional control problems."""

NEWS = (
         'May 2021: I will be joining <a href="https://mila.quebec/en/">Mila</a> and starting as an assistant professor at the <a href="https://diro.umontreal.ca/english/home/">University of Montreal</a> in August 2021! ',
         'Apr 2021: Our <a href="https://arxiv.org/abs/2103.14295">research paper</a> that will be presented at ICRA2021 on <a href="https://youtu.be/goxCjGPQH7U">RL for bipedal robots</a> was featured in <a href="https://www.technologyreview.com/2021/04/08/1022176/boston-dynamics-cassie-robot-walk-reinforcement-learning-ai/">MIT Technology Review</a>',
         'Mar 2021: Associate Editor for IROS 2021',
         'Feb 2021: Two papers accepted to ICRA2021!',
         'Jan 2021: <a href="https://people.eecs.berkeley.edu/~gberseth/projects/smirl-surprise-minimizing-rl-in-unstable-environments.html">SMiRL: Surprise Minimizing RL in Unstable Environments</a> receives  <span style="font-weight:bold;">oral presentation at ICLR 2021 (top 1.8% of submitted papers)</span>',
         'Jan 2021: Two papers accepted to ICLR 2021',
         'Jan 2021: Invited talk at IJCAI workshop Neuro-Cognitive Modeling of Humans and Environments',
         'Aug 2020: Deep Integration of Physical Humanoid Control and Crowd Navigation <span style="font-weight:bold;">receives best paper runner up at MIG2020</span>',
         'Sep 2019: Visual Imitation work featured in MIT CSAIL podcast',
         'Apr 2019: Started PostDoc at <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> group working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning Lab (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>',
         'Feb 2019: Defended Ph.D. Thesis at the University of British Columbia under the supervision of <a href="https://www.cs.ubc.ca/~van/">Michiel van de Panne</a> ',
         'Aug 2017: SIGGRAPH paper DeepLoco: Dynamic Locomotion Skills Using Hierarchical Deep Reinforcement Learning covered in the <a href="https://www.popularmechanics.com/technology/news/a27581/deeploco-deep-learning-run-bot-siggraph-2017/">Popular Mechanics</a>.',
         'Mar 2017: Awarded NSERC PhD scholarship',
         'May 2016: Modelling Dynamic Brachiation receives <span style="font-weight:bold;">best poster award</span> at Graphics Interfaces 2016',
         'Mar 2016: Robust Space-Time Footsteps for Agent-Based Steering receives <span style="font-weight:bold;">best short paper award</span> at CASA 2016',
         )

RESEARCHAREAS= ("Hierarchical Reinforcement Learning", "Unsupervised Reinforcement Learning", "Planning", "Imitation", "Life Long Learning", "EnvironmentDesign")
# DISQUS_SITENAME = "www-fracturedplane-com"
