---
Title: SteerPlex
Date: 2014-05-20 10:20
Modified: Sunday, 21. March 2017 02:06PM 
Category: Publication
Tags: CrowdSimulation, CrowdEvacuation, SteerSim
Author: Glen B
---

SteerPlex works to define a salient set of scenario features that can be used to identify the relative complexity of a steering scenario. 

## Abstract

The complexity of interactive virtual worlds has increased dramatically in recent years, with a rise in mature solutions for designing large-scale environments and populating them with hundreds and thousands of autonomous characters. The tremendous surge in the development of crowd simulation techniques has paved the way for a new research direction that aims to analyze and evaluate these algorithms. An interesting  problem that arises in this context, and that has received  little attention to date, is whether we can predict the  complexity of a steering scenario by analyzing the  configuration of the environment and the agents involved.  This is the problem we address in this paper. First, we  statically analyze an input scenario and  compute a set of  novel salient features which characterize the expected  interactions between agents and obstacles during simulation.  Using a statistical approach, we automatically derive the  relative influence of each feature on the complexity of a  scenario in order to derive a single numerical quantity of  expected scenario complexity. We validate our proposed metric  by proving a strong negative correlation between the statically computed expected complexity and the dynamic  performance of three published crowd simulation techniques  on a large number of representative  scenarios including  movingAI benchmarks.

<article style="text-align:center">
	<p>
		This video demonstrates some of the example results of parameter optimization.
	</p>
	<video controls poster="images/FirstFrameFastAttack.png" width="720" height="410">
	  <source type="video/mp4" src="projects/SteerPlex/FeatureSpace.mp4"></source>
	  <source type="video/webm" src="projects/SteerPlex/FeatureSpace.webm"></source>
	  <!-- <source type="video/ogv" src="projects/SteerFit/ParamOptFFVideo1.5.ogv"></source> -->
	  Your browser does not support the encoded video.
	</video>
</article>

## Files

### Bibtex

<p>
@inproceedings{Berseth:2013:SES:2522628.2522650, <br>
 author = {Berseth, Glen and Kapadia, Mubbasir and Faloutsos, Petros},<br>
 title = {SteerPlex: Estimating Scenario Complexity for Simulated Crowds},<br>
 booktitle = {Proceedings of Motion on Games},<br>
 series = {MIG '13},<br>
 year = {2013},<br>
 isbn = {978-1-4503-2546-2},<br>
 location = {Dublin 2, Ireland},<br>
 pages = {45:67--45:76},<br>
 articleno = {45},<br>
 numpages = {10},<br>
 url = {http://doi.acm.org/10.1145/2522628.2522650},<br>
 doi = {10.1145/2522628.2522650},<br>
 acmid = {2522650},<br>
 publisher = {ACM},<br>
 address = {New York, NY, USA},<br>
 keywords = {crowd analysis, crowd simulation, scenario complexity},<br>
} 
</p>

[comment]: <> ( [Bibtex](../files/bibtex/EnvironmentOpt.bib))
[Paper](../projects/SteerPlex/SteerPlex.pdf)
[Presentation](../presentations/SteerPlex/reveal-pres.html)
[comment]: <> ( [Code](https://github.com/FracturedPlane/EnvironmentInterface))

