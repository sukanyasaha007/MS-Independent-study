
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
