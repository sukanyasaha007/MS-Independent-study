# Summery

Generative adversarial networks (GAN) are a powerful subclass of generative models. Despite a very rich research activity leading to numerous interesting GAN algorithms, it is still very hard to assess which algorithm(s) perform better than others.

Hence, authors of this paper created a neutral and large-scale empirical study on state-of-the art models and evaluation measures. They found that most models can reach similar scores with enough hyperparameter optimization and random restarts.

This suggests that improvements can arise from a higher computational budget and tuning more than fundamental algorithmic changes. To overcome some limitations of the current metrics, they also proposed several data sets on which precision and recall can be computed.

Their experimental results suggest that future GAN research should be based on more systematic and objective evaluation procedures. Finally, they did not find evidence that any of the tested algorithms consistently outperforms the non-saturating GAN introduced in Goodfellow's Advances in Neural Information Processing Systems paper.
