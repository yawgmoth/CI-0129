import torch
import torchvision
import torch.nn as nn
import argparse
import PIL
import random

# TODO 1: Choose a digit
digit = None

# TODO 2: Change number of training iterations for classifier
n0 = 50

def to_list(img):
    return list(map(int, img.view((28*28,)).tolist()))
    
SCALE_OFF = 0    
SCALE_RANGE = 1
SCALE_01 = 2
    

def show_image(tens, imgname=None, scale=SCALE_01):
    """
    Show an image contained in a tensor. The tensor will be reshaped properly, as long as it has the required 28*28 = 784 entries.
    
    If imgname is provided, the image will be saved to a file, otherwise it will be stored in a temporary file and displayed on screen.
    
    The parameter scale can be used to perform one of three scaling operations:
        SCALE_OFF: No scaling is performed, the data is expected to use values between 0 and 255
        SCALE_RANGE: The data will be rescaled from whichever scale it has to be between 0 and 255. This is useful for data in an unknown/arbitrary range. The lowest value present in the data will be 
        converted to 0, the highest to 255, and all intermediate values will be assigned using linear interpolation
        SCALE_01: The data will be rescaled from a range between 0 and 1 to the range between 0 and 255. This can be useful if you normalize your data into that range.
    """
    r = tens.max() - tens.min()
    img = PIL.Image.new("L", (28,28))
    scaled = tens
    if scale == SCALE_RANGE:
        scaled = (tens - tens.min())*255/r
    elif scale == SCALE_01:
        scaled = tens*255
    img.putdata(to_list(scaled))
    if imgname is None:
        img.show()
    else:
        img.save(imgname)

loss_fn = torch.nn.BCELoss()

# TODO 3
# Change Network architecture of the discriminator/classifier network. It should have 784 inputs and 1 output (0 = fake, 1 = real)
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(784,1)
    def forward(self, x):
        return self.linear1(x)
       
# TODO 4
# Implement training loop for the classifier:
# for i in range(n0):
#     zero gradients
#     calculate predictions for given x
#     calculate loss, comparing the predictions with the given y
#     calculate the gradient (loss.backward())
#     print i and the loss
#     perform an optimizer step
def train_classifier(opt, model, x, y):
    pass
    
# TODO 5
# Instantiate the network and the optimizer
# call train_classifier with the training set
# Calculate metrics on the test set 
# Example: 
#      y_pred = net(x_test[y_test == 3]) calculates all predictions for all images we know to be 3s
#      (y_pred > 0.5) is a tensor that tells you if a given image was classified as your chosen digit (True) or not (False)
#      You can convert this tensor to 0s and 1s by calling .float()
#      (y_pred > 0.5).sum() will tell you how many of these predictions were true
# You are supposed to calculate:
#     For each digit from 0 to 9, which percentage of images that were of that digit were predicted as your chosen digit
#     The percentage of digits that were classified correctly (i.e. that were your digit and predicted as such, or were another digit and not predicted as your digit)
#     This last value (accuracy) should be over 90%
#     Precision (which percentage of images identified as your chosen digit was actually that digit: TP/(TP+FP))
#     Recall (which percentage of your chosen digit was identified as such: TP/(TP+FN))
def classify(x_train, y_train, x_test, y_test):
    pass
    
# Task 2 (GAN) starts here

# TODO 6: Change number of total training iterations for GAN, for the discriminator and for the generator
n = 10
n1 = 25
n2 = 25

# TODO 7
# Change Network architecture of the generator network. It should have 100 inputs (will be random numbers) and 784 outputs (one for each pixel, each between 0 and 1)
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(100, 784)
    def forward(self, x):
        return self.linear1(x)

# TODO 8
# Implement training loop for the discriminator, given real and fake data:
# for i in range(n1):
#     zero gradients
#     calculate predictions for the x known as real 
#     calculate loss, comparing the predictions with a tensor consisting of 1s (we want all of these samples to be classified as real)
#     calculate the gradient (loss_true.backward())
#     calculate predictions for the x known as fake
#     calculate loss, comparing the predictions with a tensor consisting of 0s (we want all of these samples to be classified as fake)
#     calculate the gradient (loss_false.backward())
#     print i and both of the loss values
#     perform an optimizer step
def train_discriminator(opt, discriminator, x_true, x_false):
    print("Training discriminator")

# TODO 9 
# Implement training loop for the generator:
# for i in range(n2):
#     zero gradients 
#     generate some random inputs
#     calculate generated images by passing these inputs to the generator
#     pass the generated images to the discriminator to predict if they are true or fake
#     calculate the loss, comparing the predictions with a tensor of 1s (the *generator* wants the discriminator to classify its images as real)
#     calculate the gradient (loss.backward())
#     print i and the loss
#     perform an optimization step
def train_generator(opt, generator, discriminator):
    print("Training generator")
        

# TODO 10
# Implement GAN training loop:
# Generate some random images (with torch.rand) as an initial collection of fakes
# Instantiate the two networks and two optimizers (one for each network!)
# for i in range(n):
#    call train_discriminator with the given real images and the collection of fake images 
#    call train_generator 
#    generate some images with the current generator, and add a random selection of old fake images (e.g. 100 random old ones, and 100new ones = 200 in total)
#    this will be your new collection of fake images
#    save some of the current fake images to a file (use a filename like "sample_%d_%d.png"%(i,j) so you have some samples from each iteration so you can see if the network improves)
# If you read the todos above, your training code will print the loss in each iteration. The loss for the discriminator and the generator should decrease each time their respective training functions are called 
# The images should start to look like numbers after just a few (could be after 1 or 2 already, or 3-10) iterations of *this* loop
def gan(x_real):
    show_image(x_real[0], "train_0.png", scale=SCALE_01)
    


def main(rungan):
    """
    You do not have to change this function!
    
    It will:
        automatically download the data set if it doesn't exist yet
        make sure all tensor shapes are correct
        normalize the images (all pixels between 0 and 1)
        provide labels for the classification task (0 for all images that are not your digit, 1 for the ones that are)
        extract the images of your chosen digit for the GAN
    """
    train = torchvision.datasets.MNIST(".", download=True)
    x_train = train.data.float().view(-1,28*28)/255.0
    labels_train = train.targets
    y_train = (labels_train == digit).float().view(-1,1)
    
    test = torchvision.datasets.MNIST(".", train=False)
    x_test = test.data.float().view(-1,28*28)/255.0
    labels_test = test.targets
    y_test = (labels_test == digit).float().view(-1,1)
    
    if rungan:
        gan(x_train[labels_train == digit])
    else:
        classify(x_train, y_train, x_test, y_test)
    
    
        
"""
You can pass -g or --gan to the script to run the GAN part, otherwise it will run the classification part.
"""
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Train a classifier or a GAN on the MNIST data.')
    parser.add_argument('--gan', '-g', dest='gan', action='store_const',
                        const=True, default=False,
                        help='Train and run the GAN (default: train and run the classifier only)')

    args = parser.parse_args()
    main(args.gan)