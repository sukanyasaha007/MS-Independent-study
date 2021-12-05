
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

![Untitled](GAN%20Learning%20Outcome/Untitled%201.png)

[https://arxiv.org/pdf/2009.07769.pdf](https://arxiv.org/pdf/2009.07769.pdf)

### Paper 2: Temporal Generative Adversarial Nets with Singular Value Clipping

[https://arxiv.org/pdf/1611.06624.pdf](https://arxiv.org/pdf/1611.06624.pdf)

- In this paper the Temporal GAN is used to learn a semantic representation of unlabeled videos, and is capable of generating videos.
- Usually Generative Adversarial Nets (GAN)-based methods  generate videos with a single generator consisting of 3D de-convolutional layers. This paper introduces a model that exploits two different types of generators: a temporal generator and an image generator.
- The temporal generator takes a single latent variable as input and outputs a set of latent variables each of which corresponds to an image frame in a video. The image generator transforms a set of such latent variables into a video. To deal with instability in training of GAN with such advanced networks, the authors adopted Wasserstein GAN
