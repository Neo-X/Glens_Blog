---
Title: Deep Integration of Physical Humanoid Control and Crowd Navigation
Date: 2020-10-10 10:20
Modified: Wednesday, 10. Oct 2020 02:06PM 
Category: Publication
Tags: ReinforcementLearning, HierarchicalRL
Author: Glen Berseth
Authors: Brandon Haworth, Glen Berseth, Seonghyeon Moon, Petros Faloutsos, Mubbasir Kapadia
Link: ?
Cover: <div align="center">     <table align="center">        <tr>    <td width="25%">       <img width="100%" src="/~gberseth/projects/DeepCrowds/General-Crowds-Comparison.svg">   </td>    <td width="25%">  <img width="100%" src="/~gberseth/projects/DeepCrowds/trajectory_comparisons.svg">  </td> </tr>  </table> <img width="70%" src="/~gberseth/projects/DeepCrowds/Teaser1.png"> </div>
summary: Many multi-agent navigation approaches make use of simplified representations such as a disk. These simplifications allow for fast simulation of thousands of agents but limit the simulation accuracy and fidelity. In this paper, we propose a fully integrated physical character control and multi-agent navigation method. In place of sample complex online planning methods, we extend the use of recent deep reinforcement learning techniques. This extension improves on multi-agent navigation models and simulated humanoids by combining Multi-Agent and Hierarchical Reinforcement Learning. We train a single short term goal-conditioned low-level policy to provide directed walking behaviour. This task-agnostic controller can be shared by higher-level policies that perform longer-term planning. The proposed approach produces reciprocal collision avoidance, robust navigation, and emergent crowd behaviours. Furthermore, it offers several key affordances not previously possible in multi-agent navigation including tunable character morphology and physically accurate interactions with agents and the environment. Our results show that the proposed method outperforms prior methods across environments and tasks, as well as, performing well in terms of zero-shot generalization over different numbers of agents and computation time.
comments: true
Type: Hierarchical Reinforcement Learning
TitleShort: Physical Humanoid Crowd Navigation
---

<div align="center">
	<p>
				Brandon Haworth*, Glen Berseth*, Seonghyeon Moon, Petros Faloutsos, Mubbasir Kapadia
	</p>
	<p>	
            University of Victoria, UC Berkeley, Rutgers University, York University
    </p>
</div>


Many multi-agent navigation approaches make use of simplified representations such as a disk. These simplifications allow for fast simulation of thousands of agents but limit the simulation accuracy and fidelity. In this paper, we propose a fully integrated physical character control and multi-agent navigation method. In place of sample complex online planning methods, we extend the use of recent deep reinforcement learning techniques. This extension improves on multi-agent navigation models and simulated humanoids by combining Multi-Agent and Hierarchical Reinforcement Learning. We train a single short term goal-conditioned low-level policy to provide directed walking behaviour. This task-agnostic controller can be shared by higher-level policies that perform longer-term planning. The proposed approach produces reciprocal collision avoidance, robust navigation, and emergent crowd behaviours. Furthermore, it offers several key affordances not previously possible in multi-agent navigation including tunable character morphology and physically accurate interactions with agents and the environment. Our results show that the proposed method outperforms prior methods across environments and tasks, as well as, performing well in terms of zero-shot generalization over different numbers of agents and computation time.


<div class="t">
    <table align="center">
        <tr>
    <td align="center">
        <img width="100%" src="/~gberseth/projects/DeepCrowds/General-Crowds-Comparison.svg">
        </td>
    <td>
   		<img width="100%" src="/~gberseth/projects/DeepCrowds/trajectory_comparisons.svg">
           </td>
</table>
</div>


This post is based on the following paper:

- Brandon Haworth, Glen Berseth, Seonghyeon Moon, Petros Faloutsos, Mubbasir Kapadia <br />
  [Deep Integration of Physical Humanoid Control and Crowd Navigation](/~gberseth/projects/DeepCrowds/DeepCrowds.pdf) <br />
  [Project Website](?)
