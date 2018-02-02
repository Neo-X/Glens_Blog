---
Title: Demistifying the Many Deep Rienforcement
Date: 2018-01-10 10:20
Modified: Friday, 10. Jan 2018 02:06PM 
Category: Article
Tags: RL, DeepLearning
Author: Glen Berseth
comments: true
---


#Intro

In recient years there has been an explosion in Deep Reinforcement learning research resulting in the creation of many different RL algorithms that work with deep networks. In DeepRL and RL in general the goal is to train a policy $\pi(a|s,\theta)$ with parameters $\theta$.

It is difficult to keep track of all the algorithms let alone their properties and when it is best to use which one.

In this post I am making an effort to organize a number of RL methods into a few groups. This organizing will help clear up some of the misconceptions of different algorithm and demistify what some of these properties really mean, for example, on-policy vs off-policy.


| Name        | on/off policy           |  action space support | exploration method| 
| ------------- |:-------------:| -----:| -----:|
| TRPO      | on-policy | discrete and continuous | e-greedy and Gaussian noise |
| DDPG      | off-policy      |   continuous only | Ornstein–Uhlenbeck process  |
| A3C | on-policy      | discrete and continuous | e-greedy and Guassian noise |
| CACLA | on-policy | continuous | e-greedy and Guassian noise |
| DQN | off-policy | discrete | e-greedy |
| A2C | on-policy | discrete and continuous | e-greedy and Guassian noise |
| Q-Prop | on-policy | discrete and continuous | e-greedy and Guassian noise |
| PPO | on-policy | discrete and continuous | e-greedy and Guassian noise |
| CEM | on-policy | discrete and continuous | e-greedy and Guassian noise |



### Continuous Actor Critic Learning Automaton (CACLA)

CACLA can be thought of as a simpleir policy learning algorithm that was developed before some of the recient form mathimetically methods. A citic (value function) and policy are learned at the same time (aka actor-critic method). CACLA uses the critic as a *score function* to indicate what actions the policy should learning from. In this case it is used as an indicator function, an action that performs better than the current estimate of the policies future discounted reward is given to the policy to learn from. The policy will use MSE loss to fit the network to these better than average actions.

**Pros:**

1. CACLA seems to work very well with neural networks. Being able to use a simple MSE loss for the policy makes the SGD very stable.

**Cons:**

1. Can't addjust the amount of exploration that policy should perform.
2. Original method only uses single step returns to determine if reward for action is above average.

### Asynchronous Actor Critic (A3C)

A3C is a modification of CACLA in at least two ways. The MSE loss is switch with a log likelihood loss and the score function is extanged for a multistep return estimation. Switching to a log likelihood loss allows us to model the distribution of action better using a policy. In the case of continuous actions the policy can be modeled as a vector of gaussian distributions. This in combination with the new score function that allows for a better trade-off between bias of the value function and the varaince in monte carlo samples from the simulation allows us to include a loss for the standard deviations in the policy. Now we can update the amount of exploration we think the policy should be performing in a state dependant manner.

**Pros:**

1. Using on-policy method with log likelihood loss allows the exploration to be learned.
2. Method can be parallelized well.

**Cons:**

1. In practice exploration is still a challenge. An *Entropy* term is added to the loss to help increase exploration
1. The policy mean can still change dramatically making learning a good policy challenging.
 

### Deep Deterministic Policy Gradient (DDPG)

DPG is a slightly different framework that is more like DQN. Instead of using a score function to push the policy in the direction of actions with higher reward instead a action-valued Q function is learned. This action-valued function $q(s,a)$ can be used to compute the direction to change the current action in order to increase the overall future discounted reward. Simply the method maximizes $q(s,\pi(a|s))$. However, this method does not account for how exploration should be performed. Approximating a q-function is done off-policy so the the q-function can learn the value of states and actions the policy might not explore and in doing so can better estimate the value over all actions. This property should theoretically allow for the learning of full q-function that encodes the best action to take in any state. In practice this model is learned to compute gradients over the current mean of the policy in order to improve the policy.

**Pros:**

1. Can work very well for high dimensional continuous action problems
1. Learns an action-valued function instead of a state-valued function.

**Cons:**

1. Does not explicitly provide a formalism for the exploration to be used.
1. Needs a target network to increase stability while learning action-valued function.

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

**Pros:**

1. Paralizable
1. Does not use as much memory as TRPO

**Cons:**

1. KL can still change significantly between updates. Some network tuning could be necissary.


##Discussion

There are still many more RL algorithms than the ones mentioned here. These are the ones that are popular and I am more familier with.

<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = 13; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://www-fracturedplane-com.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
