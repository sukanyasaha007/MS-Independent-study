# Week10

## Topic - Unpaired Translation with CycleGAN

Learned about how unpaired image-to-image translation differs from paired translation, learn how CycleGAN implements this model using two GANs, and implement a CycleGAN to transform between horses and zebras!

### Hands on-

Built a generative model based on the paper Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks by Zhu et al. 2017, commonly referred to as CycleGAN. I trained a model that can convert horses into zebras, and vice versa with the emphasis  on the loss functions. I trained my model starting from a pre-trained checkpoint.

### **Learning Objectives**

1. Compare paired image-to-image translation to unpaired image-to-image translation.
2. Identify how their key difference necessitates a different GAN architecture.
3. Implement unpaired image-to-image translation model, called CycleGAN, to adapt horses to zebras (and vice versa) with two GANs in one.