import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import *

class MLP_Model:
    @staticmethod
    def build():
        model = Sequential()
        
        # Первый слой 100 нейронов, 11 входных переменных
        model.add(Dense(100, input_dim=11, activation='relu'))
        
        # Второй слой 100 нейронов
        model.add(Dense(100, activation='relu'))
        
        # Третий слой 80 нейронов
        model.add(Dense(80, activation='relu'))
        
        # Выходной слой 3 выходных переменных, с активаций Relu
        model.add(Dense(3, activation='sigmoid'))

        return model