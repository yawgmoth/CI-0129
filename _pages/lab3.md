---
title: "Lab 3"
layout: single
excerpt: "Lab 3: Neural Networks"
sitemap: true
permalink: /labs/lab3.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Introduction

In this lab, we will use a neural network to classify images. You should have your code from labs 1 and 2, which we will use to read the image data and class labels and as the basis of our training loop. This lab is based on 
chapter 5.2 of "Deep Learning with PyTorch: Essential Excerpts", and you may want to refer to it for more details if anything is unclear. You may also want to refer to 
[this tutorial](https://towardsdatascience.com/building-neural-network-using-pytorch-84f6e75f9a) for the basics of defining Neural Networks in PyTorch.

## Report

You are required to document your work in a report, that you should write while you work on the lab. Include all requested images, and any other graphs you deem interesting, and describe what you observe. The lab text will 
prompt you for specific information at times, but you are expected to fill in other text to produce a coherent document. At the end of the lab, send an email with the names and carn&eacute;s of the students in the group as well
as the zip file containing the lab report as a pdf, and all code you wrote to the two professors and the assistant ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), [joseaguevara@gmail.com](mailto:joseaguevara@gmail.com), [diegomoraj@outlook.com](mailto:diegomoraj@outlook.com)) **with the subject** "\[CI-2600\]Lab 3, carn&eacute; 1, carn&eacute; 2". Do **not** include the data sets in this zip file or email. 

## Revisiting the SkillCraft1 Master Table Dataset

Take a look at your code from last week, in particular the linear model function `model`: You defined it as `w * x + b`. (Almost) the simplest possible Neural Network consists of a single neuron representing exactly the same 
function. The module `torch.nn` contains a class `Linear` which defines exactly such a neural network. Update your code to use `torch.nn.Linear(1,1)` instead of your own model function (the parameters are the number of inputs and
outputs). Instead of `w` and `b`, the neural network gives you a `parameters()` method, which you should pass to your optimizer. Check if the results are the same, better or worse than your results from last week.

Now, instead of simply using a linear model in the form of a neural network, let's make our model a bit more complex. Neural Networks in PyTorch are organized as `Module`s: To create a new neural network you have to:

  - Create a subclass of `nn.Module`
  - Initialize the neural network with its layers in the `__init__` method 
  - Implement the `forward` method which takes a tensor `x` and sequentially passes it through the layers 
  
There are many helper functions defined by PyTorch, including all common activation functions, and compositions. There is even the `nn.Sequential` container 
([documentation](https://pytorch.org/docs/master/nn.html#torch.nn.Sequential)), which can help you avoid having to define your own class for many simple tasks.

For the purpose of this lab define a simple neural network with a few neurons in one hidden layer, and try several different numbers of hidden neurons and types of activations functions and report your results on the training 
set as well as the test set. You can plot your predicted function by passing a list of ascending values for x and drawing the resulting curve.


## Useful Resources

 - [PyTorch Tensor Documentation](https://pytorch.org/docs/stable/tensors.html)
 - [Deep Learning with PyTorch: Essential Excerpts](https://pytorch.org/deep-learning-with-pytorch)
 - [Basic PyTorch operations](https://jhui.github.io/2018/02/09/PyTorch-Basic-operations/)
 - [matplotlib sample plots](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html)
