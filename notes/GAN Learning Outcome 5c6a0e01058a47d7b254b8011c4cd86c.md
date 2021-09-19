# GAN Learning Outcome

What is a GAN:

## Week1

### What is GAN

GANs are powerful models that learn to produce realistic objects that are difficult to distinguish from existing real ones, for instance, human faces. A GAN learns by making a generator and a discriminator, compete against each other. 

The generator learns to generate fakes that look real, to fool the discriminator and the discriminator learns to distinguish between what's real and what's fake. So we can think of the generator as a painting forger and the discriminator as an art inspector. So the generator forges fake images to try to look as realistic as possible, and it does this in the hopes of fooling the discriminator. Additionally, the generator isn't allowed to see the real images. It doesn't know how this painting should even look. So this is really, really tough for the generator, especially in the beginning.

### Discriminator

The discriminator is a type of classifier it models the probability of an example being fake given that set of inputs X. For instance, in a look at a picture of a Mona Lisa or a fake Mona Lisa and determine that with 85% probability this isn't the real one, 0.85 fake. 

### Generator

The generator won't output the same cat at every run, and so to ensure it's able to produce different examples every single time, you actually will input different sets of random values, also known as a noise vector. this noise vector is fed in as input, sometimes with our class y for cat into the generators neural network. 

### How it Works

First, you have a noise vector or those random input values you saw. You pass this into a generator represented by a neural network to produce a set of features that can pose an image of a cat or an attempt at a cat. Then this output is fed into the discriminator, which determines how real and how fake it thinks it is based on its inspection of it. Now we can compute a cost function that basically looks at how far the examples produced by the generator are being considered real by the discriminator because the generator wants this to seem as real as possible. Then from the difference between these two to then update the parameters of the generator, and that gets it to improve over time and know which direction to move it's parameters to generate something that looks more real and will fool the discriminator.

![Untitled](GAN%20Learning%20Outcome%205c6a0e01058a47d7b254b8011c4cd86c/Untitled.png)

## Week2

### Batch Normalization

Let's say we have cat images and the neural net has two features x1- fur size and x2 fur color. Now, the distribution of x1 can be distributed normally with very few extremely small or extremely large examples. While the distribution of fur color x2 can be skewed towards higher values with a much higher mean and lower standard deviation where higher value here represents darker fur colors. So comparing the values of fur color and size doesn't really have a meaningful correlation. 

So if NN tries to get to local minima and it has very different distributions across inputs, the cost function will be elongated. So that changes to the weights relating to each of the inputs will have  different effect on this cost function. And this makes training difficult, makes it slower and highly dependent on how weights are initialized. 

Also if new training or test data has light fur color that the distribution shifts then the form of the cost function may change too. So the location of the minimum could also move even if the ground truth of cat label is same. This is known as covariate shift. To mitigate this input variables x1 and x2 can be normalized meaning, the distribution of the input variables will have mean 0 and a standard deviation 1. Then the cost function will also look smoother and more balanced across these two dimensions. And as a result training would actually be much easier and potentially much faster.

### Pooling and Upsampling

Pooling is used to reduce the size of the input while up-sampling is used to increase the size of that input. 

Pooling is used to lower the dimension of the input images by taking the mean or finding the maximum value of different areas. For instance, a picture of a cat after a pooling layer will result in a blurry image with a lower size or lower resolution. 

Upsampling has the opposite effect of pooling. Given a lower resolution image, up-sampling has a goal of outputting one that has higher resolution. This requires inferring values for the additional pixels.

- It can be done by nearest neighbors up-sampling and using this method, one can copy the values of the pixels from the input multiple times to fill the output.
- It can also be done using linear and bi-linear interpolation which infers the values from missing pixels in the output by looking at the known values from the input.

Unlike convolutions, neither pooling nor up-sampling layers have no learnable parameters.

### DCGAN Paper

Source-

[Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)

Motivation:

In this paper authors were motivated to  build a model that can infer image representations by training Generative Adversarial Networks (GANs) and later reusing parts of the generator and discriminator networks as feature extractors for supervised tasks. GANs provide an attractive alternative to maximum likelihood techniques.

They ran experiments with a set of constraints on the architectural topology of Convolutional
GANs that make them stable to train. 

Some of the claimed contributions of this paper were-
• The authors trained discriminators for image classification tasks and showed competitive performance with other unsupervised algorithms.
• They also visualized the filters learnt by GANs and empirically showed that specific filters have
learned to draw specific objects.

### Hands on-

Implemented a simple generative adversarial network (GAN) using PyTorch

### **Learning Objectives**

1. Build the generator and discriminator components of a GAN from scratch.
2. Create generator and discriminator loss functions.
3. Train your GAN and visualize the generated images.

## Week3-

### Mode Collapse

A mode in a distribution of data is an area with a high concentration of observations. For instance, the mean value in a normal distribution is the single mode of that distribution. 

For example, take handwritten digits represented by features x_1 and x_2, meaning that these are just dimensions along which you can represent  the digits. The probability density distribution in this case will be a surface with many peaks corresponding to each digit. This is definitely multimodal with 10 different modes.

### Binary crossentropy

Binary cross entropy is a loss function that is used in binary classification tasks. These are tasks that answer a question with only two choices (yes or no, A or B, 0 or 1, left or right). Several independent such questions can be answered at the same time, as in multi-label classification or in binary [i](https://peltarion.com/knowledge-center/documentation/cheat-sheets/image-segmentation-/-mark-a-single-object-type-within-an-image-/-cheat-sheet)mage segmentation.

### WGAN

[https://arxiv.org/abs/1701.07875](https://arxiv.org/abs/1701.07875)

The 

![https://machinelearningmastery.com/wp-content/uploads/2019/05/Algorithm-for-the-Wasserstein-Generative-Adversarial-Networks-1.png](https://machinelearningmastery.com/wp-content/uploads/2019/05/Algorithm-for-the-Wasserstein-Generative-Adversarial-Networks-1.png)

### Hands on-

Implemented WGAN

In this notebook, you're going to build a Wasserstein GAN with Gradient Penalty (WGAN-GP) that solves some of the stability issues with the GANs that you have been using up until this point. Specifically, you'll use a special kind of loss function known as the W-loss, where W stands for Wasserstein, and gradient penalties to prevent mode collapse.

### Paper :  Time Series Anomaly Detection using GAN

In this paper, authors introduced TadGAN, an unsupervised anomaly detection approach built on Generative Adversarial Networks (GANs). To capture the temporal correlations of time series distributions, they use LSTM Recurrent Neural Networks as base models for Generators and Critics. TadGAN is trained with cycle consistency loss to allow for effective time-series data reconstruction. They used Gazebo, Turtlebot model and GCP. Normal data from odometer data, faulty data from having crashes, broken wheel. They go discriminator output as below-

![Untitled](GAN%20Learning%20Outcome%205c6a0e01058a47d7b254b8011c4cd86c/Untitled%201.png)

[https://arxiv.org/pdf/2009.07769.pdf](https://arxiv.org/pdf/2009.07769.pdf)

### Paper 2: Temporal Generative Adversarial Nets with Singular Value Clipping

[https://arxiv.org/pdf/1611.06624.pdf](https://arxiv.org/pdf/1611.06624.pdf)

- In this paper the Temporal GAN is used to learn a semantic representation of unlabeled videos, and is capable of generating videos.
- Usually Generative Adversarial Nets (GAN)-based methods  generate videos with a single generator consisting of 3D de-convolutional layers. This paper introduces a model that exploits two different types of generators: a temporal generator and an image generator.
- The temporal generator takes a single latent variable as input and outputs a set of latent variables each of which corresponds to an image frame in a video. The image generator transforms a set of such latent variables into a video. To deal with instability in training of GAN with such advanced networks, the authors adopted Wasserstein GAN

## Week4

### Conditional GAN

Although GAN models are capable of generating new random plausible examples for a given dataset, there is no way to control the types of images that are generated other than trying to figure out the complex relationship between the latent space input to the generator and the generated images. The conditional generative adversarial network, or cGAN for short, is a type of GAN that involves the conditional generation of images by a generator model. Image generation can be conditional on a class label, if available, allowing the targeted generated of images of a given type.

### Hands on-

Implemented cGAN to generate hand-written images of digits, conditioned on the digit to be generated (the class vector). 

### **Learning Objectives**

1. Learn the technical difference between a conditional and unconditional GAN.
2. Understand the distinction between the class and noise vector in a conditional GAN.