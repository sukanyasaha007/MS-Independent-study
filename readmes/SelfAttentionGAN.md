# Summery

This paper proposed the Self-Attention Generative Adversarial Network (SAGAN) which allows attention-driven, long-range dependency modeling for image generation tasks

Traditional convolutional GANs generate high-resolution details as a function of only spatially local points in lower-resolution feature maps

In SAGAN, details can be generated using cues from all feature locations. Moreover, the discriminator can check that highly detailed features in distant portions of the image are consistent with each other. Furthermore, recent work has shown that generator conditioning affects GAN performance. Leveraging this insight, authors applied spectral normalization to the GAN generator and find that this improves training dynamics
