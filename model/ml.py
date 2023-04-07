#### Etherscan ML model ####
# python version = 3.11.2

import tensorflow as tf


# Convolutional NN

CONV_WIDTH = 5
conv_model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(filters=32,
                           kernel_size=(CONV_WIDTH,),
                           activation='relu'),
    tf.keras.layers.Dense(units=32, activation='relu'),
    tf.keras.layers.Dense(units=1),
])
