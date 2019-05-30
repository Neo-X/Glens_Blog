---
Title: Visual Imitation with Reinforcement Learning using Recurrent Siamese Networks
Date: 2019-05-25 10:20
Modified: Thu, 25. May 2019 02:06PM 
Category: Publication
Tags: RL, DeepLearning, Simulation, Imitation Learning
Author: Glen Berseth
comments: true
---

<div align="center">
			<span class="STYLE17"> <img width="600" src="../projects/SMBAE/teaser.png"> </span>
			<span class="STYLE17"> <img width="300" src="../projects/SMBAE/teaser2.png"> </span> &nbsp; &nbsp; &nbsp;
</div>

# VIRL

Imitation learning, the ability to copy an expert’s behaviour, is a challenging and important problem. It’s what allows animals to understand and replicate observed behaviour. Many SoTA methods for imitation accomplish this via additional data that is often not available. For example, along with the experts joint positions, the torques are available as well. In this work we show for the first time a learning system that allows an agent to reproduce imitative behaviour of 3D simulated robots from video. This progress may allow us to create robots that can learn behaviour from observing humans, and allow humans to instruct robots in a natural way to perform a task.

### Distance Learning

Often, imitation is structured as a distribution matching problem where we want to minimize a distance function that differentiates between behaviour that is close to the expert demonstration. If we have access to the expert’s actions we can use semi-supervised learning to have the agent act in the world and ask the expert what it would have done. However, we rarely have access to such data in the real world. Instead, we can use our visual perceptions to observe the expert and attempt actions until what we do matches what was observed. This leads to two challenges. First, understanding if the agent’s behaviour matches the expert given only video data, by creating a meaningful distance metric. Second, getting the agent to learn the actions necessary to match the expert.

While there has been work on imitation strategies from images for manipulation [[BAIR](https://bair.berkeley.edu/blog/2018/06/28/daml/)] and 2D robots [[GoogleBrain](https://sites.google.com/view/actionablerepresentations)], the challenge of 3D imitation from video is an important milestone. Previous methods have made progress on imitation from images, by learning a transformation of images such that in this transformed space, meaningful distances are available. However, the problem of learning meaningful representations for planning or imitation is far from solved. A critical aspect of imitating a motion is the motions sequential and causal nature. The motion has both an ordering and a speed.



#### **Imitation from Sequences**

In this work we make use of the sequential structure of motion to better inform a deep reinforcement learning (RL) process. Affectively, we learn two distance functions, one in space and another in time. While the spatial distance function is designed to understand distances between pictures or poses. The time-based distance function understands if two motions look semantically similar. For example, if the imitation goal is to walk does the agents behaviour also look like a walk? In affect, with this new abstraction we can ask the question, does this motion look like a walk, not, does this motion look precisely like that walk. This allows us to reward the agent for behaviour that is similar to the expert and may just be at a different speed or time.



**Show a video a walk , another in slow motion and a fall motion (they both receive the same reward...**



#### **Siamese network**

To learn both of these distances we train a recurrent Siamese network. This method is trained with positive and negative examples. Where positive examples are similar or from the same class and negative examples are known to be different or are from different classes. The model is trained to produce similar encodings when two videos are the same and different encodings when two videos are different. Additional data is included from other tasks to assist in training the siamese network.



**Siamese network image..**



### **Results**

Using the spatial and temporal distance functions in combination we can now train RL agents to match expert demonstrations. **Show 2D video results here.** We find that the combination of distances is critical to learning good imitative behaviour from video. The new temporal distances allow quick learning but have trouble achieving high quality results without the addition of spatial rewards.



### ![img](https://lh6.googleusercontent.com/5EGPcHzDMoaQcjpKzYoDG90pE8g_eAF8Ycl2XFj9jrwtqJaZXfSV9MK9s-xmVh-BtvAkdDLnScPz2vUGVB43s5v0kiQN9WXPGOSg3dE2yNvYiAsbEvzA6ptdf2i4UYk9S9kVspyu)**Works on 3D** 

The addition of these new rewards using temporal distances (along with some additional insights) has enabled imitation learning of 3D motion imitation given only a single video demonstration. While these are the first results of its type additional quality might be gained from multi-view video data or additional multi-task data.

<iframe width="560" height="315" src="https://www.youtube.com/embed/s1KiIrV1YY4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Files

[Paper](https://arxiv.org/abs/1901.07186)







