---
Title: Optimizing Simulated Crowd Behaviour	
Date: 2014-05-20 10:20
Modified: Sunday, 21. March 2017 02:06PM 
Category: Project
Tags: CrowdSimulation, CrowdEvacuation, SteerSim, Optimization
Author: Glen Berseth
Summary: Optimizing Simulated Crowd Behaviour is the title of my master thesis and is the culmination of two pieces of work <a href="steerplex.html">SteerPlex</a> and <a href="steerfit.html">SteerFit</a>. 
---

Optimizing Simulated Crowd Behaviour is the title of my master thesis and is the culmination of two pieces of work <a href="steerplex.html">SteerPlex</a> and <a href="steerfit.html">SteerFit</a>. 

## Abstract

In the context of crowd simulation, there is a diverse set of algorithms that model steering, the ability of an agent to navigate between spatial locations, while avoiding static and dynamic obstacles. The performance of steering approaches, both in terms of quality of results and computational efficiency, depends on internal parameters that are manually tuned to satisfy application-specific requirements. This work investigates the effect that these parameters have on an algorithm's performance. Using three representative steering algorithms and a set of established performance criteria, we perform a number of large scale optimization experiments that optimize an algorithm's parameters for a range of objectives.

For example, our method automatically finds optimal parameters to minimize turbulence at bottlenecks, reduce building evacuation times, produce emergent patterns, and increase the computational efficiency of an algorithm. Our study includes a statistical analysis of the correlations between algorithmic parameters, and performance criteria. We also propose using the Pareto Optimal Front as an efficient way of modelling optimal relationships between multiple objectives, and demonstrate its effectiveness by estimating optimal parameters for interactively defined combinations of the associated objectives. The proposed methodologies are general and can be applied to any steering algorithm using any set of performance criteria.

<article style="text-align:center">
							<p>
								This video demonstrates some of the example results of parameter optimization.
							</p>
							<video width="720" height="410" controls>
							  <source type="video/mp4" src="projects/MastersThesis/Thesis-high-quality.mp4"></source>
							  <source type="video/webm" src="projects/MastersThesis/Thesis-high-quality.webm"></source>
							
							  Your browser does not support the encoded video.
							</video>
						</article>

## Files

[comment]: <> ([Bibtex](../files/bibtex/EnvironmentOpt.bib))
[Paper](///projects/MastersThesis/thesis.pdf)
[Presentation](///projects/MastersThesis/Thesis-Presentation2.pptx)
[comment]: <> ( [Code](https://github.com/FracturedPlane/EnvironmentInterface))

