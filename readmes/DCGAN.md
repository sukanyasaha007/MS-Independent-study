# Motivation

In this paper authors were motivated to  build a model that can infer image representations by training Generative Adversarial Networks (GANs) and later reusing parts of the generator and discriminator networks as feature extractors for supervised tasks. GANs provide an attractive alternative to maximum likelihood techniques.

They ran experiments with a set of constraints on the architectural topology of Convolutional
GANs that make them stable to train

## Some of the claimed contributions of this paper were

1. The authors trained discriminators for image classification tasks and showed competitive performance with other unsupervised algorithms

2. They also visualized the filters learnt by GANs and empirically showed that specific filters have
learned to draw specific objects