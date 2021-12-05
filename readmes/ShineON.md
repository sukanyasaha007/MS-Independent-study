# Summery

Virtual try-on has garnered interest as a neural rendering benchmark task to evaluate complex object transfer and scene composition. Recent works in virtual clothing try-on feature a plethora of possible architectural and data representation choices. However, they present little clarity on quantifying the isolated visual effect of each choice, nor do they specify the hyperparameter details that are key to experimental reproduction

Authors of this paper built a series of scientific experiments to isolate effective design choices in video synthesis for virtual
clothing try-on. Specifically, they investigated the effect of different pose annotations, self-attention layer placement, and activation functions on the quantitative and qualitative performance of video virtual try-on. We find that Dense Pose annotations not only enhance face details but also decrease memory usage and training time

Also, they found that attention layers improve face and neck quality. Finally,they showed that GELU and ReLU activation functions are the most effective in the experiments despite the appeal of newer activations such as Swish and Sine.
