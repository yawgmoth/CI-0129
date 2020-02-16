---
title: "Lab 4"
layout: single
excerpt: "Lab 4: Neural Networks for Classification"
sitemap: true
permalink: /labs/lab4.html
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
as the zip file containing the lab report as a pdf, and all code you wrote to the two professors and the assistant ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), [joseaguevara@gmail.com](mailto:joseaguevara@gmail.com), [diegomoraj@outlook.com](mailto:diegomoraj@outlook.com)) **with the subject** "\[CI-2600\]Lab 4, carn&eacute; 1, carn&eacute; 2". Do **not** include the data sets in this zip file or email. 


## A more complex example

Once you have familiarized yourself with the basics of Neural Networks in PyTorch it is time to move to a more interesting problem: Classifying the digits in the MNIST data set. For this task, you will need a larger neural
network. Your input comes in the form of 28x28 pixel images, which means you will have 784 inputs. The hidden layer or layers will have to "compress" this down to 10 different outputs ("one-hot-encoding"). Try different 
number of hidden neurons and even layers and different activation functions, to see which one performs best. Generally, you will want to use `Sigmoid` or `ReLU` activation functions in the hidden layers and `SoftMax` in 
the output layer, but experiment with different options. To measure performance after training, feed the **test set** to the neural network as input. This will tell you how well your network generalizes, rather than 
just measuring how much it memorizes. Use a confusion matrix to determine which digits are often mistaken for another, and calculate the per-class precision, recall and F1-scores. Note that the recall for class `i` is the 
element `(i,i)` of the confusion matrix divided by the sum of the `i`th column (actual samples of class `i`), and the precision is the element `(i,i)` of the confusion matrix divided by the `i`th row (samples predicted to be 
of class `i`). 

Once you have a performance you are happy with (you should be able to achieve at least 90% accuracy on the test set), look at your neural network. For example, each neuron in the first layer has 784 inputs, one for each 
pixel. Likewise, it has 784 weights associated with it (+ a bias). Each of these weights describes how "important" each pixel is to that particular neuron. You can look at these weights and interpret them as an image (make 
sure to rescale it so that the values are between 0 and 255). This will result in an image that describes which part of the input each neuron is "responsible for". Can you find any neurons with "obvious" responsibilities? 
What could that mean? Put any interesting pictures obtained from your weights into your report. 

Note: For the weight images, you can expect something like the images shown below, which you may interpret as neurons responsible for detecting loops (zeroes), and a combination of fives and nines. Not all neuros will have 
weights as clear as these, many will just be gray-ish blobs like the third image below. You can still identify a little black curve which this neuron identifies, but it is less clear (strong) than in the other two images.

<img src="/CI-2600/assets/img/weights1.png"><img src="/CI-2600/assets/img/weights2.png"><img src="/CI-2600/assets/img/weights3.png">


## Useful Resources

 - [PyTorch Tensor Documentation](https://pytorch.org/docs/stable/tensors.html)
 - [Deep Learning with PyTorch: Essential Excerpts](https://pytorch.org/deep-learning-with-pytorch)
 - [Basic PyTorch operations](https://jhui.github.io/2018/02/09/PyTorch-Basic-operations/)
 - [matplotlib sample plots](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html)
 - [Multi-Class metrics](https://towardsdatascience.com/multi-class-metrics-made-simple-part-i-precision-and-recall-9250280bddc2)
