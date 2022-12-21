import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *

class LSTM_Model:
    @staticmethod
    def build():
        model = Sequential()
        
        # Первый слой 20 нейронов, 11 входных переменных, так же добавили регуляризацию
        model.add(LSTM(40, input_shape=(11, 1), return_sequences = True))
        model.add(Dropout(0.2))

        # Второй слой из 50 нейронов и регуляризация
        model.add(LSTM(units = 60, return_sequences = True))
        model.add(Dropout(0.2))
        
        # Третий слой 50 нейронов и регуляризация
        model.add(LSTM(units = 40))
        model.add(Dropout(0.2))
        
        # Выходной слой 3 выходных переменных, с активаций Relu
        model.add(Dense(3, activation='relu'))

        return model