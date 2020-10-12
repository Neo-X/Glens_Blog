---
Title: KL Divergence Regularization for RL
Date: 2017-05-25 10:20
Modified: 2017-05-25 19:30
Category: ReinforcementLeanring
Tags: RL, Python, KLDivergence
Author: Glen B
---

# Intro

Regularization is a very common practice in machine learning. In supervized learning it is used to reduce model complexity. It also helps prevent the model from over fitting the test data. In RL because of the availablility of limitless data regularization does not need to be used to reduce model complexity. Instead it is used to reduce the change between policy updates. 

KL divergence has been given a lot of attention recently because it can be used in a clear way to measure the statistical divergence between two probability distributions.

KL D is not a metric however the change in kl divergence can be used measure the change in a statistical distribution.



$$ D_{KL}(\pi(a|s,\theta), \pi(a|s,\theta')) $$