---
Title: Deep Rienforcement Learning: A course on the subject 
Date: 2017-11-10 10:20
Modified: Friday, 10. Nov 2017 02:06PM 
Category: Article
Tags: RL, DeepLearning
Author: Glen Berseth
---


#Intro

In recient years there has been an explosion in Deep Reinforcement learning research resulting in the creation of many different RL algorithms that work with deep networks. In DeepRL and RL in general the goal is to train a policy \$\pi(a|s,\theta)\$ with parameters $\theta$.

It is difficult to keep track of all the algorithms let alone their properties and when it is best to use which one.

In this post I am making an effort to organize a number of RL methods into a few groups. This organizing will help clear up some of the misconceptions of different algorithm and demistify what some of these properties really mean, for example, on-policy vs off-policy.


| Name        | on/off policy           |  action space support | exploration method| 
| ------------- |:-------------:| -----:| -----:|
| TRPO      | on-policy | discrete and continuous | e-greedy and Gaussian noise |
| DDPG      | off-policy      |   continuous only | Ornstein–Uhlenbeck process  |
| A3C | on-policy      | discrete and continuous | e-greedy and Guassian noise |
| CACLA | on-policy | discrete and continuous | e-greedy and Guassian noise |
| DQN | on-policy | discrete and continuous | e-greedy and Guassian noise |
| A2C | on-policy | discrete and continuous | e-greedy and Guassian noise |
| Q-Prop | on-policy | discrete and continuous | e-greedy and Guassian noise |
| PPO | on-policy | discrete and continuous | e-greedy and Guassian noise |
| CEM | on-policy | discrete and continuous | e-greedy and Guassian noise |


**What do I want to say about each algorithm? A kind of list of important or useful properties. What do I want to convey that  epople might not normally consider an important property**

### Continuous Actor Critic Learning Automaton (CACLA)

CACLA can be thought of as a simpleir policy learning algorithm that was developed before some of the recient form mathimetically methods. A citic (value function) and policy are learned at the same time (aka actor-critic method). CACLA uses the critic as a *score function* to indicate what actions the policy should learning from. In this case it is used as an indicator function, an action that performs better than the current estimate of the policies future discounted reward is given to the policy to learn from. The policy will use MSE loss to fit the network to these better than average actions.

**Pros:**

1. CACLA seems to work very well with neural networks. Being able to use a simple MSE loss for the policy makes the SGD very stable.

**Cons:**

1. Can't addjust the amount of exploration that policy should perform.
2. Original method only uses single step returns to determine if reward for action is above average.

### Asynchronous Actor Critic (A3C)

### Deep Deterministic Policy Gradient (DDPG)



### Trust Region Policy Optimization (TRPO)

TRPO is a great algorithm with some very good theoretical properties. Stochastic policy optimization can be challenging becasue the stochasticity can change quickly. This in combination with the properties deep neural networks, in particular that deep nets like to recieve nice small gradients. When the stochasticity grows so do the gradients, when the gradients grow so to can (and usually does) the stochasticity of the policy. TRPO uses congugate gradient decent with line search to optimize the policy parameters $\theta$ will applying a constraint the the KL divergence. The KL divergence constraint assist in keeping the stochastic distribution the policy models from changing to much between updates. 

**Pros:**

1. TRPO can work very well and is known to even exibit monotonic policy improvements.

**Cons:**

1. Challenging (impossible?) to use TRPO for things like recurrent neural networks.
2. Lots of memory is needed to compute the Fisher vector product (AKA gradient vector product) of the paremters $\theta$
3. Not easily paralizable.

### Proximal Policy Optimization (PPO)

PPO was born from work that was done to combate the weaknesses of TRPO while keeping the monotonic improvements. PPO uses stochastic gradient descent instead of congugate gradient descent to optimize the policy parameters. Instead of a hard constraint on the KL divergence a soft constraint is used. This constraint has been used in the form of a boundary vilolation penalty and a clipping term (the official version). PPO has been shown to have close to or better performance than TRPO.

**Cons:**