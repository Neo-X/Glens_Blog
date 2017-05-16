---
layout: post
title: Using SWIG to wrap C++ for Python
date: '2017-05-14T00:25:00.001-07:00'
author: Glen B
tags: 
---

# Intro

These days many people want to use one of many new libraries written in python to train deep learning models.
In general Python has many powerful and easy to use libraries for performing machine learning. 
However, many appications that generate data that we want to learn are written in other languages.
In particular many simulators for RL applications are written in C++.
Here I am going to focus on an interface I have found useful for wrapping physics-based simulators in C++.

## The Interface

We want to able to support two types of control flow.
One for learing and one for simulation.

For Rendering the simulation:
```
callback Animate
    For n = 1 .. num_substeps
    Check if needs new action
        get state()
        get new action
        apply the action
    
    update sim

    postredisplay()
```


For Simulating for Training:
```
act(action)
apply the action
    While (not needsNewAction)
        update sim()

simEpoch(actor, env)
    n=0
    While (not endOfEpisode() or n < 100)
        S = env.getState()
        A = policy(s)
    R  = env.act(a)
        Tuples[n] = (S, A, R)
        n+=1

    output_queue.put(Tuples)
```

## The code

```
/*
 * SimbiconWrapper.h
 *
 *  Created on: Dec 9, 2016
 *      Author: Glen
 */

#ifndef SRC_SIMBICONADAPTER_SIMBICONWRAPPER_H_
#define SRC_SIMBICONADAPTER_SIMBICONWRAPPER_H_

#include <simbiconAdapter/UI.h>
// #include "Environment.h"
#include "Configuration.h"
#include <vector>
#include "SimbiconAgent.h"
#include <Core/SimBiController.h>


class SimulationWrapper {
public:

    /// Create the wrapper given some configuration
	SimulationWrapper(Configuration * config);
	virtual ~SimbiconWrapper();
    /// Get the Current observation the agent can 'see'
	virtual std::vector<double> getObservation();
	virtual bool endOfEpoch();
	// virtual double act(Action) = 0;
	virtual double act(std::vector<double> action);
	virtual double updateAction(std::vector<double> action);
	/// Perform on simulation update
	virtual void update();
	/// check whether or not the last action has completed and a new action is needed
	virtual bool needUpdatedAction();

	virtual std::vector<double> getSimState();
	virtual void setSimState(std::vector<double> state_);
	virtual std::vector<double> getStateFromSimState(std::vector<double> state_);


	virtual void init();
	virtual void initEpoch();
	virtual void generateEnvironmentSample();
	virtual std::vector<double> getEvaluationData();

	// virtual void numAction();
	// virtual void numStats();

	virtual void finish();
	virtual void clear();

	virtual void start(double in);
	virtual void stop();

	virtual SimbiconAgent * getActor() const {return _actor;}
	/// Has the agent fallen (into a non recoverable state)
	virtual bool agentHasFallen();
	/// tester BVH file parsing
	virtual void parseBVH(std::string filename);

	virtual double calcReward() const ;

	/// Interactive functions to doing things in the simulation, like reseting and throwing objects at the character
	virtual void onKeyEvent(int key, int mouseX, int mouseY);

private:
	SimbiconAgent * _actor;

	virtual double _actSimbicon(std::vector<double> action);
	virtual double _actPDTargets(std::vector<double> action);
	virtual double _calcImitationReward() const;
	virtual double _calcVelocityReward() const;

};

#endif /* SRC_SIMBICONADAPTER_SIMBICONWRAPPER_H_ */

```


