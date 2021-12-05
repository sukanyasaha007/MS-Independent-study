# Summery

PixelRNN is an example of the auto-regressive Generative Model.

In the era of social media, plenty of images are out there. But it’s extremely difficult to learn the distribution of natural images in an unsupervised setting. PixelRNN is capable of modeling the discrete probability distribution of image and predict the pixel of an image in two spatial dimensions.

We all know that RNNs are powerful in learning conditional distribution, especially  LSTM is good at learning the long-term dependency in a series of pixels. This formulation works in a progressive fashion where the model predicts the next pixel Xi+1 when all pixels X0 to Xi are provided.

Compared to GANs, Auto-regressive models like PixelRNN learn an explicit data distribution where GANs learn implicit probability distribution. Because of that GAN doesn’t explicitly expose the probability distribution rather allows us to sample observation from the learned probability distribution.

The architechture consists of individual residual blocks of pixelRNN. It’s trained up to several depths of layers. The input map to the PixelRNN LSTM layer has 2h features. The input-to-state component reduces the number of features by producing h features per gate. After applying the recurrent layer, the output map is upsampled back to 2h features per position via a 1 × 1 convolution and the input map is added to the output map.
