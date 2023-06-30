### Neural Net building for Ethereum gas probability matrix ###
# python version = 3.11.2
# libraries

from tensorflow import keras
from keras import layers
from keras.models import model_from_json
from app.prob_dt import dt_prep_train
from app.prob_dt import dt_prep_pred
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

# train or recreate the neural net
def train_nn():
    # path to where ethereum trasaction data recorded
    path = os.getenv('PATH_D')
    # get training data
    input_d, output_d = dt_prep_train(path)
    input_d = input_d.reshape((21, 2, 12*240))
    output_d = output_d.reshape((21, 12*240))

    try:
        with open('app/eth_nn_model.json', 'r') as file:
            model_json = file.read()

        # Load the model architecture from the JSON file
        model = model_from_json(model_json)

        # Load the model weights
        model.load_weights('app/eth_nn_model_weights.h5')

        # compile the model
        model.compile(
            loss=keras.losses.mean_squared_error,
            optimizer = keras.optimizers.Adam(learning_rate=1e-4),
            metrics = ['RootMeanSquaredError']
        )

        # Retrain the model with new data
        model.fit(input_d, output_d, batch_size=8, epochs=20, verbose=2)

        # save the trained model
        with open('app/eth_nn_model.json', 'w') as file:
            file.write(model.to_json())

        # Save the updated model weights to an HDF5 file
        model.save_weights('app/eth_nn_model_weights.h5')

    except:
        # NN model
        model = keras.Sequential()
        model.add(keras.Input(shape=(None, 12*240)))
        model.add(
            layers.Bidirectional(
                layers.LSTM(1024, return_sequences=True, activation='tanh')
            )
        )
        model.add(layers.LSTM(1024, activation='tanh'))
        model.add(layers.Dense(12*240))

        # compile the model
        model.compile(
            loss=keras.losses.mean_squared_error,
            optimizer = keras.optimizers.Adam(learning_rate=1e-4),
            metrics = ['RootMeanSquaredError']
        )

        # train model with new data
        # Retrain the model with new data
        model.fit(input_d, output_d, batch_size=8, epochs=20, verbose=2)

        # save the trained model
        with open('app/eth_nn_model.json', 'w') as file:
            file.write(model.to_json())

        # Save the updated model weights to an HDF5 file
        model.save_weights('app/eth_nn_model_weights.h5')
    
    msg = "Neural net retrining completed."
    return msg

# predict the probability matrix for next hour
def pred_nn():
    # path to where ethereum trasaction data recorded
    path = os.getenv('PATH_D')

    input_dt = dt_prep_pred(path)
    input_dt = input_dt.reshape((1,2,12*240))

    try:
        with open('app/eth_nn_model.json', 'r') as file:
            model_json = file.read()

        # Load the model architecture from the JSON file
        model = model_from_json(model_json)

        # Load the model weights
        model.load_weights('app/eth_nn_model_weights.h5')

        # compile the model
        model.compile(
            loss=keras.losses.mean_squared_error,
            optimizer = keras.optimizers.Adam(learning_rate=1e-4),
            metrics = ['RootMeanSquaredError']
        )

        # predict for the next hour
        pred = model.predict(input_dt)
        pred = pred.reshape((12, 240))
        pred = np.where(pred > 1, 1, pred)
        pred = np.where(pred < 0, 0, pred)
        return pred
    
    except:
        msg = "No trained model to be found. Try to train a model first."
        return msg