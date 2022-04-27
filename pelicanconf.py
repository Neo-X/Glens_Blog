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
         ('Teaching', SITEURL_ + '/teaching-new-course-in-robot-learning.html'),
         ('Google Scholar', 'https://scholar.google.ca/citations?user=-WZcuuwAAAAJ&hl=en'),
         ('twitter', "https://twitter.com/GlenBerseth"),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('twitter', 'https://twitter.com/GlenBerseth'),)

DEFAULT_PAGINATION = 5

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

    I am an assistant professor at the <a href="https://diro.umontreal.ca/accueil/">Université de Montréal</a>, a core academic member of the <a href="https://mila.quebec/en/">Mila - Quebec AI Institute</a>, <a href="https://cifar.ca/ai/canada-cifar-ai-chairs/">CIFAR AI chair</a>, and co-director of the <a href="https://montrealrobotics.ca/">Robotics and Embodied AI Lab (REAL)</a>. 
    I was a Postdoctoral Researcher with <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a>, working with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>. 
    His previous and current research has focused on solving sequential decision-making problems for real-world autonomous learning systems (robots). 
    The specific of his research has covered the areas of reinforcement-, continual-, meta-, hierarchical learning, and human-robot collaboration. 
    In his work, Dr. Berseth has published at top venues across the disciplines of robotics, machine learning, and computer animation. 
    Currently, he is teaching a course on robot learning at Université de Montréal and Mila that covers the most recent research on machine learning techniques for creating generalist robots. 
 <br>
 <br> 
 To see a more formal biography, click <a href="biography.html">here</a>.
 <table>
 <tr><td>
 <h4>Interested in joining <a href="https://montrealrobotics.ca/">the lab?</a></h4>
 </tr></td>
 <tr><td>
     Are you interested in the practical and theoretical challenges of creating generalist problem-solving robots? Please see <a href="./contact.html">this page</a> to apply. I may not respond to emails.
 </tr></td>
 </table>
"""

SITESUBTITLE = """I am an assistant professor at the <a href="https://diro.umontreal.ca/">University de Montreal</a> and <a href="https://mila.quebec/en/">Mila</a>. My research explores how to use deep learning and reinforcement learning to develop generalist robots."""

NEWS = (
         'Apr 2022: <a href="https://nouvelles.umontreal.ca/en/article/2022/04/19/the-fondation-courtois-gives-159m-to-udem-for-the-discovery-of-new-materials/">UdeM receives 159M</a> to create the <a href="https://institut-courtois.umontreal.ca/en/">Courtois Institute</a> to support fundamental science and apply AI and robotics to scientific experimentation. My lab will lead research on methods for automating scientific experimentation.',
         'Jan 2022: New paper accepted to ICLR on <a href="https://arxiv.org/abs/2112.04467">Continual Meta-Reinforcement Learning</a>.',
         'Sep 2021: New paper accepted to CoRL on <a href="https://sites.google.com/view/relmm">autonomous robot learning</a>!',
         'Sep 2021: New paper accepted to NeurIPS on <a href="https://sites.google.com/view/ic2/home">surprise minimization in partially observed environments</a>!',
         'Sep 2021: I will be teaching a course on <a href="http://www.fracturedplane.com/teaching-new-course-in-robot-learning.html"> deep reinforcement learning for robotics</a> in January 2022!',
         'May 2021: I will be joining <a href="https://mila.quebec/en/">Mila</a> and starting as an assistant professor at the <a href="https://diro.umontreal.ca/">University of Montreal</a> in August 2021!',
         'Apr 2021: Our <a href="https://arxiv.org/abs/2103.14295">research paper</a> that will be presented at ICRA2021 on <a href="https://youtu.be/goxCjGPQH7U">RL for bipedal robots</a> was featured in <a href="https://www.technologyreview.com/2021/04/08/1022176/boston-dynamics-cassie-robot-walk-reinforcement-learning-ai/">MIT Technology Review</a>',
         'Mar 2021: Associate Editor for IROS 2021',
         'Feb 2021: Two papers accepted to ICRA2021!',
         'Jan 2021: <a href="http://www.fracturedplane.com/projects/smirl-surprise-minimizing-rl-in-unstable-environments.html">SMiRL: Surprise Minimizing RL in Unstable Environments</a> receives  <span style="font-weight:bold;">oral presentation at ICLR 2021 (top 1.8% of submitted papers)</span>',
         'Jan 2021: Two papers accepted to ICLR 2021',
         'Jan 2021: Invited talk at IJCAI workshop Neuro-Cognitive Modeling of Humans and Environments',
         'Aug 2020: Deep Integration of Physical Humanoid Control and Crowd Navigation <span style="font-weight:bold;">receives best paper runner up at MIG2020</span>',
         'Sep 2019: Visual Imitation work featured in MIT CSAIL podcast',
         'Apr 2019: Started PostDoc at <a href="https://bair.berkeley.edu/">Berkeley Artificial Intelligence Research (BAIR)</a> group working in the <a href="http://rail.eecs.berkeley.edu/">Robotic AI & Learning Lab (RAIL)</a> lab with <a href="https://people.eecs.berkeley.edu/~svlevine/">Sergey Levine</a>',
         '...'
         )

# RESEARCHAREAS= ("Hierarchical Reinforcement Learning", "Unsupervised Reinforcement Learning", "Planning", "Imitation", "Life Long Learning", "EnvironmentDesign")
RESEARCHAREAS= ("Representative", )
# DISQUS_SITENAME = "www-fracturedplane-com"
