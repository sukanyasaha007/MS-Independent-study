

## Week4

### Conditional GAN

Although GAN models are capable of generating new random plausible examples for a given dataset, there is no way to control the types of images that are generated other than trying to figure out the complex relationship between the latent space input to the generator and the generated images. The conditional generative adversarial network, or cGAN for short, is a type of GAN that involves the conditional generation of images by a generator model. Image generation can be conditional on a class label, if available, allowing the targeted generated of images of a given type.

### Hands on-

Implemented cGAN to generate hand-written images of digits, conditioned on the digit to be generated (the class vector). 

### **Learning Objectives**

1. Learn the technical difference between a conditional and unconditional GAN.
2. Understand the distinction between the class and noise vector in a conditional GAN.