"""Optimizing with TensorBoard
By: 
- Changing optimizer (adam), within the optimizer (learning rate)
- Changing Dense layer (have or dont have)
- How many units per layer, activation unit
- Changing kernel size, stride
- Changing decay rate
Basic things:
- Number of layer
- Nodes per layer
- Do we have a Dense layer at the end or not
Results:
3 conv layer + 0 dense layer are the best

Notes: 500k images data will help to improve accuracy
We need use trail-error to find the best model and check whether we have negative data
or not (Negative data are data that do not enable us to reject our null hypothesis)
"""
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
import os

directPath = os.getcwd()


X = pickle.load(open(directPath + "\\X.pickle", "rb"))
y = pickle.load(open(directPath + "\\y.pickle", "rb"))
X = X/255.0

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# In this case a model with zero dense layer seems to be better
# In other cases, model might work better with 256 or 512 layer nodes for 1 dense layer
# or it just memorize more data and overfit
dense_layers = [0, 1, 2]
# Common layer sizes, up to the user
layer_sizes = [32, 64, 128]
# Cannot have zero conv layer
conv_layers = [1, 2, 3]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer, layer_size, dense_layer, int(time.time()))
            # Throw the tensorboard here
            tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))
            print(NAME)
            model = Sequential()

            # First layer needs to have input_shape no matter what
            # First dense layer that we see have to have a Flatten
            # Leave the first one like this
            model.add(Conv2D(layer_size, (3,3), input_shape=X.shape[1:]))
            model.add(Activation("relu"))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            # After the Conv layer, we gonna have a Flatten
            for l in range(conv_layer-1):
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation("relu"))
                model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Flatten())

            for l in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation("relu"))

            # Need a dense layer before the output layer
            model.add(Dense(1))
            model.add(Activation("sigmoid"))

            model.compile(loss="binary_crossentropy",
                          optimizer="adam",
                          metrics=['accuracy'])
            model.fit(X, y, batch_size=32, epochs=10, validation_split=0.1, callbacks=[tensorboard])


