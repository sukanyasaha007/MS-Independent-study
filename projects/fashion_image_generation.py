import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.optimizer import Adam
from tennsorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, BatchNormalization, LeakyReLU, Dropout, Input, Reshape
# Dense is the fully conneted layer
import tensorflow.datasets
# fashion mnist of 70k images (grey scale 28x28x1)

def build_disc(input_shape= (28, 28, 1), summary= True):
    model = Sequential()
    model.add(Input(shape=input_shape))
    model.add(Flatten())
    model.add(Dense(512))
    model.add(LeakyReLU((.2)))
    model.add(Dense(256))
    model.add(LeakyReLU((.2)))
    model.add(Dense(1), activation= "sigmoid")

    if summary:
        model.summary()
    return model

def build_generator(z_dim=(100), output_shape= (28, 28, 1), summary=True):
    model = Sequential()
    model.add(Input(shape= z_dim))
    model.add(Dense(256))
    model.add(LeakyReLU(.2))
    model.add(BatchNormalization(momentum= .8))
    model.add(Dropout())
    model.add(Dense(512))
    model.add(LeakyReLU(.2))
    model.add(BatchNormalization(momentum = .8))
    model.add(Dense(1024))
    model.add(LeakyReLU(.2))
    model.add(BatchNormalization(momentum = .8))
    model.add(Dense(np.prod(output_shape), activation= "tanh"))
    model.add(Reshape(output_shape))

    if summary:
        model.summary()
    return model

print("generating")
gen= build_generator()
noise= tf.random.normal([1, 100])
generated_img= gen(noise, training=False)
print("show image")
plt.imshow(generated_img[0, :, :, 0], cmap= "gray")
plt.show()