---
layout: post
title: Putting a steering algorithm into SteerSuite
date: '2013-04-17T14:52:00.001-07:00'
author: Glen B
tags: 
modified_time: '2013-04-17T14:52:59.230-07:00'
blogger_id: tag:blogger.com,1999:blog-2030049895335802245.post-8644504171274397206
blogger_orig_url: http://fracturedplane.blogspot.com/2013/04/putting-steering-algorithm-into.html
---

<br /><br />This is a guide I created which I hope to turn into a Wiki some day on how to put your steering algorithm in SteerSuite.<br /><br /><ol><li>First things first</li><ol><li>Your agent needs to extend the SteerLib::AgentInterface class so that is can be used properly with the gspacialDatabase</li><li>If your algorithm keeps collections of obstacle types or other agents the types should be changed to SteerLib::AgentInterface or other agents and SteerLib::BoxObstacle</li><li>Next you will need to start converting geometries</li><ol><li>If you are lucky the algorithm that is being ported to SteerSuite will differentiate between Points and Vecotors otherwise you will need to go through every operation and check if it produces a Point or Vectory because SteerSuite differentiate between them.</li></ol><li>The *AIModule should not include the Agent type</li><ol><li>This is to avoid circular includes</li><li>Not should the agent include the module type only the interfaces provided from SteerSuite</li></ol><li>Try not to change any of the math in the algorithm</li><ol><li>Best is to alter the initial conditions to fit the algorithm best and then convert the reusult computed by the algorithm back into SteerSuite coordinates. </li></ol></ol></ol>