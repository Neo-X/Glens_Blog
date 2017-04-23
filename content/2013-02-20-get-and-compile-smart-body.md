---
layout: post
title: Get and Compile Smart Body
date: '2013-02-20T17:03:00.000-08:00'
author: Glen B
tags: 
modified_time: '2013-02-21T06:43:50.056-08:00'
blogger_id: tag:blogger.com,1999:blog-2030049895335802245.post-334321633855013237
blogger_orig_url: http://fracturedplane.blogspot.com/2013/02/get-and-compile-smart-body.html
---

This page is linked to another and will outline the steps to get and compile SmartBody.<br /><br />Current svn command and link<br /><br /><pre class="prettyprint"><code class="language-bash"><br />svn co https://smartbody.svn.sourceforge.net/svnroot/smartbody/trunk smartbody&nbsp;<br /></code></pre><br /><br />To Compile for Windows follow the steps in the guide that basically just say to use visual studio to open the solution and build the project.<br /><br />For Linux it was a little more complicated. I prefer to work on Linux (Ubuntu) for my work so I ventured on writing a script to setup all of the dependencies.<br /><br /><a href="http://www.cse.yorku.ca/~glenpb/files/install_smartbody_dependancies" target="_blank">Here</a> is a script I wrote to setup all the dependencies for SmartBody on Ubuntu 12.04.<br /><br />