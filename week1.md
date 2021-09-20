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

![Untitled](GAN%20Learning%20Outcome/Untitled.png)