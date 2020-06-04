---
title: "Lab 4"
layout: single
excerpt: "Lab 4: Neural Networks"
sitemap: true
permalink: /labs/lab4.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

Lab 4: Neural Networks, deadline: Jul 3

## Introduction

In this lab, we will use a neural network to classify images, and then *generate* more images of the same type. This lab is based on 
chapter 5.2 of ["Deep Learning with PyTorch: Essential Excerpts"](https://pytorch.org/deep-learning-with-pytorch), and you may want to refer to it for more details if anything is unclear. You may also want to 
refer to [this tutorial](https://towardsdatascience.com/building-neural-network-using-pytorch-84f6e75f9a) for the basics of defining Neural Networks in PyTorch.

The general idea of the lab is split into two tasks: First, you will build a classifier, that is able to identify one particular, handwritten digit (for example 2s) to learn the basics about Neural Networks in PyTorch, 
and how to use them. In the second task, you will build a second neural network that takes random numbers as its input and uses them to produce a **new** image of a 2. Each of these neural networks is trained using a 
target to calculate a **loss**. For the classifier, the loss is defined by how many digits it classifies wrongly (2s that are not identified as such, and other digits that are classified as 2s), while the generator uses 
the classifier to calculate its loss: The more generated images the classifier identifies as "fake", the higher the loss of the generator. The two networks will therefore play a "game": The classifier (also called 
"discriminator") will become better and better at identifying "real" 2s, while the generator will become better and better at deceiving the discriminator. 

To get started with this lab, install pytorch as described on their [website](https://pytorch.org/get-started/locally/) (if you have doubts, use "Stable", your OS, "pip", and "Cuda 10.2"). You will need a 64bit installation
of Python 3! If you have hardware limitations, and can't install these requirements, contact the instructor, who can provide you with remote access to a machine at ECCI. Once you have installed torch, download 
[this python file](/CI-0129/assets/lab4.py) to get started. It will download and load the data set (**note**: The download is about 10MB in size, and it will uncompress to about 100MB), show you some basics of 
pytorch and provides a function to show or store images, which will be useful in this lab. The file also has clearly marked and numbered "TODO" sections for the parts you have to change, and the lab text will 
refer to these todos!

## Image Classification

For the first part of this lab, you will construct a neural network to identify one particular digit. First, choose a digit; it can be your birthday, last digit of your carn&eacute;, your favorite number, etc. (TODO 1)
To train your neural network, you will use the tensor `x_train` as the training examples, and the tensor `y_train` as the desired output of the network: `y_train` will be `1` for each 
image that is of your chosen digit, and `0` for all others (`labels_train` tells us which image is of which digit). `y_test` is created in the same fashion for the test set. The code already does this (in `main`)

Now construct a neural network for this task. Your input comes in the form of 28x28 pixel images, which means you will have 784 inputs. The hidden layer or layers will have to "compress" this down to a single output, 
representing whether the input is an image of your chosen digit or not. Start with a `LeakyReLU` activation function in your hidden layer with 256 neurons and a `Sigmoid` activation function in your output layer (TODO 3).  
Once 
you have your neural network, you need to train it. First, observe that you can pass more than one input into your network, and it will produce one output for each input. For example, if you have 100 images, you can 
pass a matrix with 100 rows (number of images) and 784 columns (number of pixels in each image) to the network, and it will produce a matrix with 100 rows, and 1 column (because you have one output for each input image). 
**Note:** The input and output will **always** be a matrix. Even if you only want to pass one image through the neural network, you have to pass it a matrix with 1 row and 784 columns and you will get a matrix with 1 row 
and 1 column as result. When in doubt, check the `shape` attribute of your input tensor: It has to have **two** dimensions.

For the actual training, you will use a loop. Implement the function `train_classifier` (TODO 4), as follows:

```Python
for i in range(n0):
    # reset gradients from previous iteration 
    opt.zero_grad()
    
    # pass training examples through network to
    # get the current prediction 
    y_pred = model(x_train)
    
    # Calculate the loss: difference between the
    # current prediction and the true label 
    loss = loss_fn(y_pred, y_train)
    
    # Calculate the gradient of the loss 
    loss.backward()
    
    # Let the optimizer update the weights
    # using the gradients
    opt.step()
```

Start with about 50 iterations, and increase when you think your code works (TODO 2).

In order to use this loop, you will need an optimizer `opt`; Use `torch.optim.Adam` (see [the documentation](https://pytorch.org/docs/stable/optim.html) for details on 
how to use an optimizer). Adam needs a starting learning rate, but it will automatically adapt it over time, so you can just start with something like `0.01`, and not worry too much about it (later you can tweak 
this value). Implement the function `classify` that instantiates the neural network and the optimizer, calls `train_classifier` and then calculates the performance of the trained network on the test set (TODO 5):

To determine the performance of your neural network, calculate the accuracy (which percentage of images was classified correctly), the precision (which percentage of images identified as your chosen digit were actually 
that digit), and the recall (which percentage of your chosen digit was identified as such). You should be able to achieve at least 90% accuracy on the test set. Using the test set, determine which digits are most often 
mistaken for yours, and vice versa. For example, if you picked 2 as your digit, for each of the other digits count how often they were classified as a 2 (false positives).

Experiment with different number of hidden neurons and even layers and different activation functions, to see which one performs best. Generally, you will 
want to use `Sigmoid` or `LeakyReLU` activation functions in the hidden layers and `Sigmoid` in the output layer, but experiment with different options for the hidden layers. To measure performance after training, feed 
the **test set** to the neural network as input. This will tell you how well your network generalizes, rather than just measuring how much it memorizes. 

Hints:
  - The existing code performs a so-called **normalization**, by dividing every pixel by 255. The result is that every input value will be between 0 and 1. Do not change this!
  - You can perform many operations on entire tensors. For example `(y_pred > 0.5).float()` will turn your prediction into a tensor of 0s and 1s, depending on whether the prediction was less than or equal to 0.5 or not. 
  - Tensors also have methods to calculate `sum`, `mean` and `abs`. There is also `min` and `max`, which can also calculate the minimum and maximum along a particular dimension (e.g. to calculate the maximum value for 
    each row), **and** tell you at which index this element was found. You may want to keep [the documentation](https://pytorch.org/docs/stable/tensors.html) handy.
  - You can use a bool tensor to index another tensor. For example `y_train == 3` will tell you which images are 3s by producing a tensor that is `True` for each image that is of a 3 and `False` for all others. You 
    can select all images that are 3s with `x_train[y_train == 3]`. This can be particularly useful to determine how each digit was classified by the neural network.
  - `show_image` can be used to display or even store an image to a file. The function has a parameter `scale` that you have to set to `SCALE_01` to undo the normalization, or the image will just be black.
  - It is a good idea to print the `loss` in every iteration of the loop. If your training process works, the loss should steadily decrease, to below 0.1. If your loss does not go below 1 after even a few iterations, 
    try reducing the learning rate.

## Generative Adversarial Networks

For the second task, construct a second network that is responsible for generating new images from random inputs as a "mirror" of your classification network. For example, if your classifier has 3 hidden layers 
with 512, 256, and 128 neurons, your generator should have 3 hidden layers with 128, 256, and 512 neurons, with similar activation functions. The generator should use 100 inputs, and produce 28*28 = 784 outputs (TODO 7).
To generate new images, these two networks "play a game" against each other, where the generator has the goal of producing images that look as realistic as possible, and the discriminator has to determine which 
images were produced by the generator and which are real.

## Training the GAN

To train your GAN, you will need two functions: One to train the generator and one to train the discriminator. First, implement the function `train_discriminator`,
which you can pass a tensor with real images and a tensor with fake images (TODO 8). Let your discriminator predict the labels for both sets of data, and calculate the
loss with `loss_fn`, calculate the gradients of the parameters and perform an optimization step (Note: this is very similar to the training loop before, but you will have **two** sets of inputs:
One consisting entirely of images you know to be real, and one consisting entirely of images you know to be fake. Call the network twice, once for each set, and compare to a tensor of all 1s for the 
real images, and a tensor of all 0s for the fake images to calculate the two losses). You can test this function with some random images/tensors (generated with `torch.rand`), and 
some images from the MNIST data set.

Then implement the function `train_generator` that samples random noise, passes it to the generator, and then passes the generated images on to the discriminator, and calculates the loss afterwards 
(**Caution**: For the generator your goal is for the predictor to predict these images as **real**), then calculate the gradient and perform an optimization step (TODO 9).

Finally, implement the function `gan` That first instantiates the two networks, and an optimizer for each, and some random fake images to start with. The training itself consist of an outer loop, 
and in each iteration, you first train the discriminator, then the generator and then add some new fake images to the training set for the discriminator:

```Python
x_false = torch.rand((100,784))

for i in range(n):
    train_discriminator(opt_d, discriminator, x_real, x_false)
    train_generator(opt_g, generator, discriminator)
    
    # generate 100 new fakes
    new_fakes = generator(torch.randn((100,100))).detatch()
    
    # Generate 100 random indices to keep
    keep_idx = torch.randperm(x_fake.size(0))[:100]
    
    # Select the images to keep
    x_keep = x_fake[keep_idx]
    
    # Concatenate the images to keep with the new fakes
    x_false = torch.cat((x_keep, new_fakes))
    
    # select one random new fake to save (you can also store more)
    j = random.randint(0,100)
    show_image(new_fakes[], "sample_%d_%d.png"%(i,j), scale=SCALE_01)
```

Notes:
  - Use `Adam` as the optimizer for both networks
  - You may have to use a *very* low learning rate (0.0001 or less), especially if you notice that your generator error is 0, and the discriminator error is 1.
  - You should `.detach()` after you create fake images for training the generator so that you don't unnecessarily calculate the gradients on the generator as well
  - Don't forget to `.zero_grads()`
  - The fact that pytorch accumulates gradients is actually useful when training the generator: You can pass both image sets (fake and real) separately, calculate the loss on each, 
    call `backward()` each time and you'll have the total gradient.
  - One of the most common problems with GANs is that all produced images are identical or nearly identical (called "mode collapse"), because the generator has found the "perfect" image to fool 
    the discriminator. Unfortunately, the only thing you can do when that happens is to restart training (perhaps with a lower learning rate) and hope to get a different/better initialization.
    Dropout layers (with probabilities of 0.5 even) in the generator may also help.

Perform this training and inspect the resulting images. Use a low n1 and n2 (around 20) at the beginning until you are sure that your code works and the loss actually decreases. Then increase these 
values. For the overall n, you will need very few iterations (less than 100). Don't forget to include some sample images in your report, but also provide an estimate of what percentage 
of images "looks decent", in your opinion. Once you have everything working, go back, and change the selection of which digit to generate (e.g. if you started with generating 2s, generate 4s now). 
You should be able to do this by changing the digit in a single place (in TODO 1), and everything else should work the same way.

## Submission

You are required to document your work in a report, that you should write while you work on the lab. Include all requested images, and any other graphs you deem interesting, and describe what you observe. The lab text 
prompts you for specific information at times, but you are expected to fill in other text to produce a coherent document. Send the finished code (all python files you have!), and your report pdf in a zip file by 
email to me and Christian ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), [aiexistencialrisk@gmail.com](mailto:aiexistencialrisk@gmail.com)). Use `[CI-0129]Lab 4, carné 1 carné 2` as the subject line. 
Do not forget to put the names and carn&eacute;'s of both team members in the report as well! **Do not include the data set** in this zip file or email.


## Useful Resources

 - [PyTorch Tensor Documentation](https://pytorch.org/docs/stable/tensors.html)
 - [Deep Learning with PyTorch: Essential Excerpts](https://pytorch.org/deep-learning-with-pytorch)
 - [Basic PyTorch operations](https://jhui.github.io/2018/02/09/PyTorch-Basic-operations/)
 - [matplotlib sample plots](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html)
 - [Multi-Class metrics](https://towardsdatascience.com/multi-class-metrics-made-simple-part-i-precision-and-recall-9250280bddc2)
