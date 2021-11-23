---
Title: Feedback Control for Cassie with Deep Reinforcement Learning
Date: 2018-09-25 10:20
Modified: Thu, 25. September 2018 02:06PM 
Category: Publication
Tags: RL, DeepLearning, Simulation, ModelBasedRL
Author: Glen Berseth
Cover: <div align="center"> <img width="27%" src="/projects/Cassie_IROS/teaser2.png">			<img width="26%" src="/projects/Cassie_IROS/teaser.png">	<img width="44%" src="/projects/Cassie_IROS/teaser3.png"> </div>
Authors: Zhaoming Xie, Glen Berseth, Patrick Clary, Jonathan Hurst, Michiel van de Panne
Summary: Deep reinforcement learning has achieved great strides in solving challenging motion control tasks. Recently, there has been significant work on methods for exploiting the data gathered during training, but there has been less work on how to best generate the data to learn from. For continuous action domains, the most common method for generating exploratory actions involves sampling from a Gaussian distribution centred around the mean action output by a policy. Although these methods can be quite capable, they do not scale well with the dimensionality of the action space, and can be dangerous to apply on hardware. We consider learning a forward dynamics model to predict the result, $(x_{t+1})$, of taking a particular action, $(u_{t})$, given a specific observation of the state, $(x_{t})$. With this model we perform internal look-ahead predictions of outcomes and seek actions we believe have a reasonable chance of success. This method alters the exploratory action space, thereby increasing learning speed and enables higher quality solutions to difficult problems, such as robotic locomotion and juggling
comments: true
Type: Imitation
TitleShort: Imitation on Cassie robot
---

<div align="center">
	<p>	
            University of British Columbia
    </p>
</div>


<div align="center">
			<span class="STYLE17"> <img width="200" src="/projects/Cassie_IROS/teaser2.png"> </span>
			<span class="STYLE17"> <img width="200" src="/projects/Cassie_IROS/teaser.png"> </span>
			<span class="STYLE17"> <img width="350" src="/projects/Cassie_IROS/teaser3.png"> </span>
			 &nbsp; &nbsp; &nbsp;

</div>

IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2018)

Zhaoming Xie (1), Glen Berseth (1), Patrick Clary (2), Jonathan Hurst (2), Michiel van de Panne (1)

(1) University of British Columbia
(2) Oregon State University  


# Abstract

Bipedal locomotion skills are challenging to develop. Control strategies often use local linearization of the dynamics in conjunction with reduced-order abstractions to yield tractable solutions. In these model-based control strategies, the controller is often not fully aware of many details, including torque limits, joint limits, and other non-linearities that are necessarily excluded from the control computations for simplicity. Deep reinforcement learning (DRL) offers a promising model-free approach for controlling bipedal locomotion which can more fully exploit the dynamics. However, current results in the machine learning literature are often based on ad-hoc simulation models that are not based on corresponding hardware. Thus it remains unclear how well DRL will succeed on realizable bipedal robots. In this paper, we demonstrate the effectiveness of DRL using a realistic model of Cassie, a bipedal robot. By formulating a feedback control problem as finding the optimal policy for a Markov Decision Process, we are able to learn robust walking controllers that imitate a reference motion with DRL. Controllers for different walking speeds are learned by imitating simple time- scaled versions of the original reference motion. Controller robustness is demonstrated through several challenging tests, including sensory delay, walking blindly on irregular terrain and unexpected pushes at the pelvis. We also show we can interpolate between individual policies and that robustness can be improved with an interpolated policy. 


## Files

[Paper](/projects/Cassie_IROS/2018-IROS-cassie.pdf)

## Videos!

<iframe width="560" height="315" src="https://www.youtube.com/embed/z3DMKQwt68Y" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

On real robot

<iframe width="560" height="315" src="cassie.mp4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Bibtex

```
@inproceedings{2018-IROS-cassie,
  title={Feedback Control for Cassie with Deep Reinforcement Learning},
  author={Zhaoming Xie and Glen Berseth and Patrick Clary and Jonathan Hurst and Michiel van de Panne},
  booktitle = {Proc. IEEE/RSJ Intl Conf on Intelligent Robots and Systems (IROS 2018)},
  year={2018}
}
```

### Acknowledgements

We thank the anonymous reviewers for their helpful feedback. This research was funded in part by an NSERC Discovery Grant (RGPIN-2015-04843).

