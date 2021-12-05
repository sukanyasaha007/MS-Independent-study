# Summery

Traditional autoencoders are models (usually multilayer artificial neural networks) designed to output a reconstruction of their input. Specifically, autoencoders sequentially deconstruct input data into hidden representations, then use these representations to sequentially reconstruct outputs that resemble the originals. Fittingly, this process of teasing out a mapping from input to hidden representation is called representation learning.

Variational Autoencoders (VAEs) incorporate regularization by explicitly learning the joint distribution over data and a set of latent variables that is most compatible with observed datapoints and some designated prior distribution over latent space. The prior informs the model by shaping the corresponding posterior, conditioned on a given observation, into a regularized distribution over latent space (the coordinate system spanned by the hidden representation).

VAEs are an excellent tool for manifold learning—recovering the “true” manifold in lower-dimensional space along which the observed data lives with high probability mass—and generative modeling of complex datasets like images, text, and audio—conjuring up brand new examples, consistent with the observed training set, that do not exist in nature.

An end-to-end autoencoder (input to reconstructed input) can be split into two complementary networks: an encoder and a decoder. The encoder maps input to a latent representation, or so-called hidden code. The decoder maps the hidden code to a reconstructed input value.

Whereas a vanilla autoencoder is deterministic, a Variational Autoencoder is stochastic—a mix of:

a probabilistic encoder, approximating the true (but intractable) posterior distribution , and a generative decoder, which does not rely on any particular input. Both the encoder and decoder are artificial neural networks (i.e. hierarchical, highly nonlinear functions) with tunable parameters.

Learning these conditional distributions is facilitated by enforcing a plausible mathematically-convenient prior over the latent variables, generally a standard spherical Gaussian.

Given this conjugate prior, the encoder’s job is to supply the mean and variance of the Gaussian posterior over each latent space dimension corresponding to a given input. Latent  is sampled from this distribution, then passed to the decoder to be transformed back into a distribution over the original data space.

In other words, a VAE represents a directed probabilistic graphical model, in which approximate inference is performed by the encoder and optimized alongside an easy-to-sample generative decoder. For this reason, these complementary halves are also known as the inference (or recognition) network and the generative network. By reformulating this graphical model as a differentiable neural net with a single, cost function (derived from the variational lower bound), this can be trained by stochastic gradient descent (SGD).
