---
title: "Lab 2"
layout: single
excerpt: "Lab 2: Learning as Model Fitting"
sitemap: true
permalink: /labs/lab2.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Introduction

In this lab, we will use data collected from players in StarCraft II to predict the number of actions per minute of a new player. Note: This lab is essentially chapter 4.1 of "Deep Learning with PyTorch: Essential Excerpts", 
and you may want to refer to it for more details if anything is unclear.

## Report 

You are required to document your work in a report, that you should write while you work on the lab. Include all requested images, and any other graphs you deem interesting, and describe what you observe. The lab text will 
prompt you for specific information at times, but you are expected to fill in other text to produce a coherent document. At the end of the lab, send an email with the names and carn&eacute;s of the students in the group as well
as the zip file containing the lab report as a pdf, and all code you wrote to the two professors and the assistant ([markus.eger.ucr@gmail.com](mailto:markus.eger.ucr@gmail.com), [joseaguevara@gmail.com](mailto:joseaguevara@gmail.com), [diegomoraj@outlook.com](mailto:diegomoraj@outlook.com)) **with the subject** "\[CI-2600\]Lab 2, carn&eacute; 1, carn&eacute; 2". Do **not** include the data sets in this zip file or email. 

## The SkillCraft1 Master Table Dataset

The [SkillCraft1 Master Table Dataset](https://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset) contains information collected from [StarCraft 2](https://starcraft2.com/en-us/) replay files and includes a measure of player activity. Basically, the researchers noted when the screen was moving, and when it was at rest and used that to determine when the players were focusing on something. The delay between when the screen came to a rest and when the player actually performed an action is called the *Action Latency*. An important measure for player skill in StarCraft 2 are the player's actions per minute (APM). All other things being equal, a player that can perform more actions per minute has an advantage. It would be reasonable to assume that a lower latency also means a higher number of actions per minute, which we will investigate in this lab.

Your first task is to read the data set from the provided CSV file and put the data into tensors. We will need two tensors: One for the input (the column `ActionLatency`) and one for the variable we want to predict (the column `APM`). Implement a function `read_csv` that takes a file name, and two column names and returns two tensors, one for each of the columns. Split the data into three sets: Use the first 30 entries as test set 1, then split the 
rest randomly into 20% test set and 80% training set. Plot each of the sets in a scatter plot using matplotlib.
  
## Fitting a Linear Model

Recall that a linear model has the general form 

$$
M(x) = y = w\cdot x + b
$$

In our case, x is the action latency, and y are the actions per minute. Your task is to find "good" values for w and b. First, write a function `model` that accepts three tensors, `w`, `x` and `b` and returns the value for `y`.
Then, write a function `loss_fn` that takes a tensor containing output values y from our model, and another tensor containing observed output values, and computes the mean squared distance between the two
 (i.e. for each pair, calculate the difference and square it, then calculate the mean value over the entire tensor). 

Mathematically, our loss function has the form: 

$$
L(\hat{\vec{y}}) = \text{mean} (\vec{y} - \hat{\vec{y}})^2
$$

In order to actually learn good values for the model parameters w and b, we will use an optimization procedure, namely gradient descent. In order to minimize the loss, we calculate it for some parameter values, and then 
"move" in the direction in which the loss decreases. This "movement" is done by changing the parameters w and b appropriately, and the direction in which the loss decreases is calculated using the gradient. What we 
want to calculate are the partial derivatives:

$$
\frac{\partial }{\partial w} L(M(x)) = \frac{1}{n} \cdot \frac{\partial }{\partial w} (y - M(x))^2 = \frac{1}{n} \cdot \frac{\partial }{\partial w} (y - (w\cdot x + b))^2\\\\
\frac{\partial }{\partial b} L(M(x)) = \frac{1}{n} \cdot \frac{\partial }{\partial b} (y - M(x))^2 = \frac{1}{n} \cdot \frac{\partial }{\partial b} (y - (w\cdot x + b))^2
$$

For this, we use the chain rule

$$
\frac{\partial }{\partial w} f(g(x)) = \frac{\partial }{\partial g(x)} f(g(x)) \cdot \frac{\partial }{\partial w} g(x)
$$

In our case, we have: 

$$
\frac{\partial }{\partial w} L(M(x)) = \frac{1}{n} \cdot \frac{\partial }{\partial M(x)} L(M(x)) \cdot \frac{\partial }{\partial w} M(x) = \frac{1}{n} \cdot 2\cdot(y - M(x)) \cdot x\\\\ 
\frac{\partial }{\partial b} L(M(x)) = \frac{1}{n} \cdot \frac{\partial }{\partial M(x)} L(M(x)) \cdot \frac{\partial }{\partial b} M(x) = \frac{1}{n} \cdot 2\cdot(y - M(x)) \cdot 1 
$$

What does this tell us? First, we "randomly" choose starting values for w and b (you can just try 1 and 0, for example), then we calculate the gradient (which tells us the direction of ascent), and then we move in the 
other direction (to descend/minimize). However, we need to be careful how far we move, and for that we introduce a constant called the "learning rate" alpha. 

$$
w' = w - \alpha \cdot \frac{\partial }{\partial w} L(M(x))\\\\
b' = b - \alpha \cdot \frac{\partial }{\partial b} L(M(x))\\\\
$$

Implement functions `dmodel_w`, `dmodel_b`, `dloss_m`, corresponding to the partial derivatives of the model and the loss function, and then implement a function `training(n, w, b, alpha, x, y)`:

Do `n` times:
  1. Calculate the current estimate for y using the current values for w and b, as well as the loss 
  2. Calculate the gradient
  3. Print the current loss, gradient and iteration count
  4. Update w and b using the gradient
  
After the loop, return the values of w and b. For now, use a constant number for `n` (e.g. 1000 iterations), and guess values for `w`, `b`, and `alpha` (**Important**: Even though `w` and `b` are just single numbers, make sure 
that they are tensors with one entry!). When you call this function using the training set as x and y, and run this loop, you should see the loss gradually decrease, until a time when it does not change much anymore. If 
not, especially if the loss is increasing over time: Try changing the learning rate. Note this in your report, and how you determined a good learning rate. Another issue that may come up: `w` and `b` use very different 
scales (`w` should be between -5 and 5, `b` will grow to over `200`), so if you set your learning rate to a low value, `b` will take forever to be updated properly, but if you set it to a high value, `w` will "blow up". 
In practice, you will try to **normalize** your inputs, so that they are (roughly) between -1 and 1. Create a new variable `xn` that is a copy of `x`, where you subtract the mean and divide by half of the range of values. 
Try using this new `xn` for as a parameter to `training` and note any differences you notice. 

Create another plot that contains the training data as a scatterplot like before, and add the learned model (line) to it. What is the loss? Is it a good fit? 
Also plot the model compared to the two test sets, and calculate their corresponding loss values. Does the model generalize well to the test set?

## Automated Gradients and Optimization

In practice, our models will be a lot more complex than simple lines, and calculating gradients by hand, while possible, is a bit annoying. Fortunately, PyTorch can automatically calculate gradients for us! All you have to do
is add an additional parameter `requires_grad=True` when you create the tensors `w` and `b` (that's why they have to be tensors!). Create a new function `training_auto`, which is a copy of the original training function, but 
instead of calculating the gradient manually, you can have PyTorch caculate it automatically as an attribute of `w` and `b`:

Recall that every tensor "remembers" where it comes from. When you calculate the loss the resulting tensor knows that it is the result of `w` and `b`, which require a gradient. You can then call `backward()` on the loss tensor, 
which will cause PyTorch to **backpropagate** the gradient and accumulate it in the leaves (in our case `w` and `b`). Then, you can access it as the `.grad` attribute of `w` and `b`. There are two pitfalls:

- The gradient will **accumulate**, which means you have to manually set it back to zero on every iteration (call `w.grad.zero_()`, but make sure `w.grad` is not `None`!)
- When you update `w` and `b`, they will be the results of tensor operations, so they will **also track** where they are coming from (namely the old `w` and `b`), which would mean that you will keep the entire history of 
computation in memory (and calculate the gradients for everything). In order to "break" this connection, call the "detach" method on `w` and `b` **after** the update, **and** also call `requires_grad_()` in order to reenable 
the gradient calculation.

This new version of the training function should behave exactly like the old one, with one big advantage: We can now use **any** (differentiable) function as our model without having to calculate the gradient manually!

Finally, the combination of calculating the gradient and updating some model parameters to minimize a loss function is so common that PyTorch also provides support for it: Optimizers. In fact, one challenge with optimization 
is that you may run into a local minimum (in our toy example the loss function does not have any local minima, so we avoided that problem), and there are also different ways of using the learning rate, adding additional 
parameters, etc. PyTorch therefore provides not just the simple gradient descent that we used, but several different kinds of optimizers with different advantages and trade-offs. The common API for them consists of the 
constructor, which takes a list of parameters to optimize (in our case `w` and `b`) and a learning rate `lr`, a method called `step`, which updates the parameters using the calculated gradients, and a method called `zero_grad`,
 which you have to call to reset the gradients. Implement a new function `training_opt`, which uses the optimizer `SGD` ("Stochastic Gradient Descent") in the following loop:
 
Do `n` times: 
   1. Call `zero_grad` on the optimizer
   2. Calculate the current estimate for y using the current values for w and b, as well as the loss  
   3. Print the current loss, gradient and iteration count
   4. Call the `step` method of the optimizer

As before, plot the learned line with this method. Is it the same as before? Better, worse? Why? How does it behave on the test sets?

Also try a different optimizer, such as `ADAM`, using the scaled as well as the unscaled data.

## A Better Fit

As you may have noticed, the data itself is not exactly suited for a linear model. As a last step, come up with a better family of functions to model the behavior of the data. Write a new function `training_nonlin`, which uses 
a new model `model_nonlin`, which should be a parameterized function, and performs the optimization procedure using that function's parameters. You could use something like:

$$
y = a\cdot x^b + c
$$

or 

$$
y = a\cdot e^{b\cdot x} + c
$$

Where a, b, and c are the model parameters. Try several different functions, and note which produced the best fit in your report. **Always** perform your training on the training data, and calculate the performance on the 
test sets!

## Useful Resources

 - [PyTorch Tensor Documentation](https://pytorch.org/docs/stable/tensors.html)
 - [Deep Learning with PyTorch: Essential Excerpts](https://pytorch.org/deep-learning-with-pytorch)
 - [Basic PyTorch operations](https://jhui.github.io/2018/02/09/PyTorch-Basic-operations/)
 - [matplotlib sample plots](https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html)
