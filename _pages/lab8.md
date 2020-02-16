---
title: "Lab 8"
layout: single
excerpt: "Lab 8: Deep Q Learning"
sitemap: true
permalink: /labs/lab8.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Introduction

In this lab, we will revisit both Q-Learning and Neural Networks to build a reinforcement learning agent that solves a task in Minecraft. We will use [malmoenv](https://pypi.org/project/malmoenv/), which is a python 
library that connects to Minecraft and exposes it as a gym environment (similar to the PoleCart task from last week).

## Report 

You are required to document your work in a report, that you should write while you work on the lab. Include all requested images, and any other graphs you deem interesting, and describe what you observe. The lab text will 
prompt you for specific information at times, but you are expected to fill in other text to produce a coherent document. At the end of the lab, send an email with the names and carn&eacute;s of the students in the group as well
as the zip file containing the lab report as a pdf, and all code you wrote to the two professors and the assistant. 

## AI Gym

To get started download [this zip file]() from the class website, which contains `minecraft.py` and some levels. It will create the gym environment and set up a training loop. Before you run this file, you will need to 
start Minecraft, which is most easily done using `python -c "import malmoenv.bootstrap; malmoenv.bootstrap.launch_minecraft(9000)"` (make sure you are in the Minecraft directory). Wait until Minecraft shows the main menu, 
and then run `minecraft.py`. It will load a map, and run an agent. Like last week, this agent will move around randomly at first. The goal of the task is to reach the gold block that is somewhere in the room. In contrast 
to last week, you will not get any explicit information about the environment, instead the observations will be exactly the pixels that are visible on the screen. The actions the agent can perform are: Do nothing, move 
forward, turn left and turn right.

## Deep Q-Learning

As described above, the agent observes the pixels from the screen, which in our case is a 320x240 window, with three color channel, for a total of 230400 entries with values from 0 and 255 in the observation vector. Creating 
a Q-Table for this problem will therefore be infeasible, even if we cleverly compress pixels. However, a Q-Table is really just an approximation to the Q-function, and there are other ways we can approximate functions: 
Neural Networks! In this lab, you should build a neural network that takes the 230400 values that make up the screen, plus an encoding of the four possible actions, and approximates the entry the Q-Table would have in that 
cell. Then you can use this neural network exactly like you used the Q-Table last time: When you have to decide on an action, you use the one that results in the highest result. The training data of your network will consist 
of the reward information that you get from the simulation. For this task you have total freedom to explore different options, but as a general guideline you will likely want some 
[Convolutional layers](https://pytorch.org/docs/stable/nn.html#conv2d), which are special units that are **not** fully connected to the previous layer, but instead look at an n-by-n "neighborhood". This is particularly useful
for things like images (which we have), where each neuron only looks at a subset of the input image. Make sure to document what you tried, and any observations you made. Also describe the architecture of the neural network 
you ended up with. Note: Unlike the previous labs, this lab is a lot more open-ended, and it is possible that your agent will not perform as well as you'd like.

## Levels

You may have noticed the "level"-parameter to the `main` function. If you find a setup that you believe works well on the basic room layout, try training a network for the higher levels. At level 2, there is still only one 
room, but it is bigger, while levels 3 to 5 consist of multiple rooms, and will therefore be harder to beat.

If you really want to challenge yourself, try levels 6-10, which include tasks other than simply finding the goal, such as crafting items (which requires resource gathering), or building structures. We will likely not have 
enough time to fully train agents for these scenarios, but if you find the tasks interesting, feel free to experiment at home, and discuss your findings with the instructors. If you enjoy this kind of task, there are 
[competitions](https://www.aicrowd.com/challenges/neurips-2019-minerl-competition) with the goal of obtaining diamonds in an actual Minecraft world using the same environment as this lab.

## Useful Resources
  
  - [Deep Q-learning](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)
  
  - [A Comprehensive Guide to Convolutional Neural Networks](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)
