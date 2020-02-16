---
title: "Lab 5"
layout: single
excerpt: "Lab 5: Generative Adversarial Networks"
sitemap: true
permalink: /labs/lab5.html
frontpageorder: 5
categories: []
---

* TOC
{:toc}

## Introduction

In this lab, we will *generate* new images based on the images in the MNIST data set using a Generative Adversarial Network. You should reuse the code from labs 1 and 4 to read the MNIST data set, write image files, and 
as the basis for the classifier. We recommend that you limit yourself to images with a single digit first (e.g. only use 8s), because it will be easier to train the network this way. Once you have the training code up and 
running, you can try using all images. [This article](https://medium.com/ai-society/gans-from-scratch-1-a-deep-introduction-with-code-in-pytorch-and-tensorflow-cb03cdcdba0f) contains a description
of how to train a GAN for the MNIST data set, if you get lost. Do **not** just copy the source code from the article, our structure is slightly different and if you don't know what you are doing, it will not work. If you 
understand what you are copying, **clearly mark** which source code was not written by you. Plagiarism will not be tolerated and will result in 0 points. [Here](https://github.com/soumith/ganhacks) you can also find some tips and tricks to make your GANs work better.

## Report

You are required to document your work in a report, that you should write while you work on the lab. Include all requested images, and any other graphs you deem interesting, and describe what you observe. The lab text will 
prompt you for specific information at times, but you are expected to fill in other text to produce a coherent document. At the end of the lab, send an email with the names and carn&eacute;s of the students in the group as well
as the zip file containing the lab report as a pdf, and all code you wrote to the two professors and the assistant ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), [joseaguevara@gmail.com](mailto:joseaguevara@gmail.com), [diegomoraj@outlook.com](mailto:diegomoraj@outlook.com)) **with the subject** "\[CI-2600\]Lab 5, carn&eacute; 1, carn&eacute; 2". Do **not** include the data sets in this zip file or email. 

## Generative Adversarial Networks

As discussed in class, a GAN consists of two separate neural networks: A generator and a discriminator. These two networks "play a game" against each other, where
the generator has the goal of producing images that look as realistic as possible, and the discriminator has to determine which images were produced by the
generator and which are real. Define two classes `Generator` and `Discriminator` as subclasses of torch.nn.Module and populate them with layers. As a start, use
three hidden layers with `LeakyReLU` and an output layer with `Tanh` (Generator) or `Sigmoid` (Discriminator) activation functions. Typically, you will want the
number of units to increase sequentially in the hidden layers of the generator (e.g. 256, 512, 1024) and the reverse sequence in the hidden layers of the
discriminator.

The input to the generator should be a vector of 100 (random) numbers, and the output will be an image with the dimensions of an MNIST image (28x28). The input for the discriminator will be an image (28x28), and the 
output will be a single classification: fake or not fake. 

## Training

To train your GAN, you will need two functions: One to train the generator and one to train the discriminator. First, write a function `train_discriminator`,
which you can pass a list of real images and a list of fake images. Let your discriminator predict the labels for both sets of data, and calculate the
loss with `nn.BCELoss()`, calculate the gradients of the parameters and perform an optimization step. Test this function with some random images/tensors (generated with `torch.rand`), and 
some images from the MNIST data set.

Then write a function `train_generator` that first samples random noise, passes it to the generator, and then passes the generated images on to the discriminator, and calculates the loss afterwards (**Caution**: For the generator your goal is for the predictor to predict these images as **real**), then calculate the gradient and perform an optimization step.

Notes:
  - Use `Adam` as the optimizer for both networks
  - You should `.detach()` after you create fake images for training the generator so that you don't unnecessarily calculate the gradients on the generator as well
  - Don't forget to `.zero_grads()`
  - The fact that pytorch acculumates gradients is actually useful when training the generator: You can pass both image sets (fake and real) separately, calculate the loss on each, perform two `backward()` passes and you'll have the total gradient.

Perform this training for a couple hundred epochs and inspect the resulting images. Don't forget to include some sample images in your report, but also provide an estimate of what percentage of images "looks decent", in 
your opinion.


## Useful Resources

 - [PyTorch Tensor Documentation](https://pytorch.org/docs/stable/tensors.html)
 - [Deep Learning with PyTorch: Essential Excerpts](https://pytorch.org/deep-learning-with-pytorch)
 - [Basic PyTorch operations](https://jhui.github.io/2018/02/09/PyTorch-Basic-operations/)
 - [matplotlib sample plots](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html)
