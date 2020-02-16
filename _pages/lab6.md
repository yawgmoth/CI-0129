---
title: "Lab 6"
layout: single
excerpt: "Lab 6: Reinforcement Learning"
sitemap: true
permalink: /labs/lab6.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Introduction

In this lab, we will implement Q-Learning and apply it to the [OpenAI Gym](https://gym.openai.com/) CartPole task. The goal of the task, which is also known as an inverse pendulum is to keep a pole that's attached to a cart 
in an upright position, as shown [here](https://gym.openai.com/envs/CartPole-v1/). The problem modeled by this task underlies the principles of things like Segways and hoverboards, as well as humanoid robots, and while 
there are analytical solutions to the problem, our approach will solve it without any knowledge of physics!

## Report

You are required to document your work in a report, that you should write while you work on the lab. Include all requested images, and any other graphs you deem interesting, and describe what you observe. The lab text will 
prompt you for specific information at times, but you are expected to fill in other text to produce a coherent document. At the end of the lab, send an email with the names and carn&eacute;s of the students in the group as well
as the zip file containing the lab report as a pdf, and all code you wrote to the two professors and the assistant ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), [joseaguevara@gmail.com](mailto:joseaguevara@gmail.com), [diegomoraj@outlook.com](mailto:diegomoraj@outlook.com)) **with the subject** "\[CI-2600\]Lab 3, carn&eacute; 1, carn&eacute; 2".

## AI Gym

To get started download [q_learning.py](/CI-2600/assets/q_learning.py) from the class website. It will create the gym environment and set up a training loop. For each episode, the simulation will keep going until the pole is more than 12-15 degrees 
from the upright position, or the cart is more than 2.4 units from the center. Your goal is to extend the duration of each episode. If you run the code as-is, you will see a visualization of the task, and the training 
process. The agent you are given simply selects a move at random (with `env.action_space.sample()`), and will therefore not perform very well (or learn anything). The output of the script tells you how long the agent 
manages to balance the pole, and you will see that most episodes last between 10 and 20 steps before the pole falls down. For this lab, agents that can somewhat consistently balance the pole for more than 50 steps are good, 
and more than 100 steps is great (The "official" criterion for solving the task is an average score of 195 over 100 episodes). Note that even the random agent may manage episodes with more than 50 steps every once in a 
while, but it will be very rare. Your agent should be more consistent: Scores of over 40 on average over 100 runs are "good", over 50 is great.

 Every step your agent has to choose between two actions: move to the left, or move to the right, encoded as 0 and 1. When the action is performed, you get an observation consisting of four 
values:

 - The x-position of the cart, between -4.8 and 4.8
 - The x-velocity of the cart, between -Inf and Inf 
 - The angle of the pole, between -24 and 24 degrees
 - The velocity of the pole at the top, between -Inf and Inf

## Q-Learning

For this task, you should implement an agent that uses Q-Learning to master the task. To do this, you will need to store a Q-Table, and update the values for each state/action pair. However, note that each observation 
consists of four floating point values, which could result in a potentially very large state space. Instead of using the raw values, you should put each of them into different bins. For example, for the distance, you may
decide that having bins for less than -1, between -1 and 0, between 0 and 1, and more than 1, is reasonable, since the cart should generally stay near the center anyway. For the other values, inspect the observations 
during the episodes and decide how to best put them into bins (use between 3 and 10 bins per variable). Next, you need to implement two functions: `select`, which returns the best action for a given state in the 
Q-table and `update`, which updates the entry of the last visited state according to the Q-learning equation:

$$
Q^{\text{new}}(s_t,a_t) \leftarrow (1-\alpha) Q(s_t,a_t) + \alpha \cdot \left(r_t + \gamma \cdot \max_a Q(s_{t+1}, a) \right)
$$

This means, after the update the value consists of a mixture of the old value, and a new value consisting of the reward plus the discounted estimated future reward. For now, guess values for $$\alpha$$ and $$\gamma$$, and see 
how your agent does. But do not just use the action returned by `select`! Instead, choose this action with probability $$1 - \varepsilon$$, where you choose $$\varepsilon$$ as something around 0.1.

## Parameter Tuning

With this implementation, your agent should do "something", but it may need very long, or fail completely, to get good results. This is the point where you should investigate its behavior. For example, after each episode you 
can inspect the Q-table: How many states does the agent "know" about? Did it learn to perform something reasonable in them? For example, in states in which the pole is tilted to the left, the agent will likely need to move 
to the left as well in order to "catch" the pole. There are several issues that can mess with the agent's ability to learn proper actions. For one, at the beginning of the training process, the agent knows nothing about the 
task, so if you choose a low $$\alpha$$ the update process of the Q-Table will need a long time to reach good value. However, once the agent has some experience with the task, you don't want the Q-Table to change dramatically 
anymore. A solution for this is to use an adaptive value for $$\alpha$$: Start with a high value, and after every episode decrease $$\alpha$$ a bit, until it reaches some minimum threshold. $$\varepsilon$$, on the other hand,
controls how many new states the agent explores during training, and like with $$\alpha$$, you will want to explore more states at the beginning of the training process, and then favor the states that you already know to be 
good. Earlier, you also somewhat arbitrarily divided the observations into parts. Now is the time to play with the values you used for the bins, and see if that improves the agent's performance.

Finally, while you have four observations, that does not mean that you will need all of them! Try omitting one or two of them. For example, the x-velocity of the cart may not actually add much information, since you will want 
the cart to be relatively slow at all times. Make sure to discuss the different options you tried in your report, and any observations you made about the behavior of the agent.

In your report you should also have a characterization of the behavior your agent learned. Do **not** just include the Q-Table, but instead summarize it in an appropriate form!

## Useful Resources

  - [Q-learning](https://towardsdatascience.com/q-learning-54b841f3f9e4)
  
  - [OpenAI Gym's Cart-Pole Balancing using Q-learning](https://mc.ai/openai-gyms-cart-pole-balancing-using-q-learning/)
  
  - [Cart-Pole Balancing with Q-Learning](https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947)
