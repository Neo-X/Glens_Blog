
---
Title: Robust Space-time Footsteps for Agent-based Steering
Date: 2014-05-20 10:20
Modified: Sunday, 21. March 2017 02:06PM 
Category: Publication
Tags: RealTimePlanning, CrowdSimulation, SteerSim
Author: Glen B
---

<article>
	<table width="100%">
		<tr width="100%">
			<td width="45%" align="center">
				<img src="../projects/RobustFootsteps/FootstepRandomizedSteps.svg" width="300px"/>
				<p>
					Randomized, continuous footstep action space.
				</p>
			</td>
			
			<td width="45%" align="center">
				<img src="../projects/RobustFootsteps/footstepStuckCorner-2.svg" width="300px"/>
				<p>
					Geometric validation to ensure valid configuration.
				</p>
			</td>
		</tr>
	</table>
</article>

With this work we build upon prevous work to inductavely design a robust footsteps-based steering algorithm. The steering algorithm uses an A* algorithm to generate least cost footstep plans between goals while avoiding dynamic collisions. 

## Abstract

A number of  recent agent-based steering methods abandon the standard particle  abstraction of an agent's locomotion abilities, and employ more complex models from timed footsteps to physics-based controllers. These models often provide the action space of an optimal search method that plans a sequence of steering actions for each agent that minimize a performance criterion.  The transition from particle based models to  more complex ones is not straightforward and gives rise to a number of technical challenges. For example, a particle representation is  constant, symmetric and convex, while a footstep model maybe  non-convex and dynamic. In this paper, we discuss our recent experience with a few of specific issues, and how we addressed them in the context of space-time footstep planning for steering virtual humans.


<article style="text-align:center">
<p>
	This video demonstrates some of the example results of robust footsteps algorithm.
</p>
<video width="720" height="410" controls>
  <source type="video/mp4" src="projects/RobustFootsteps/Footsteps_Robust.mp4"></source>
  <source type="video/webm" src="projects/RobustFootsteps/Footsteps_Robust.webm"></source>
  							
  Your browser does not support the encoded video.
</video>
</article>

<article style="text-align:center">
<h2 class="paperTitle">
	Recieved CASA2015 Best Short Paper Award
</h2>
<img src="projects/RobustFootsteps/Best_Short_Paper.jpg" width="100%"/>

<p>
	Photo - From Left to Right: Glen Berseth and Prof Jian Jun Zhang
</p>
</article>


## Files

[Bibtex](../files/bibtex/robustFootsteps.bib)
[Paper](../projects/RobustFootsteps/robustfootsteps.pdf)
[Presentation](../projects/RobustFootsteps/RobustFootstepSteering-Compressed.pptx)
[comment]: <> ( [Code](https://github.com/FracturedPlane/EnvironmentInterface))

