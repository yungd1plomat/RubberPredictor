import keras
import numpy as np
from keras.models import load_model

model_choose = input("Выберите модель для тестирования (1 - LSTM, 2 - MLP): ")
if model_choose == "1":
    model = load_model('models/lstm.model')
else:
    model = load_model('models/lstm.model')

while True:
    inp = input("Введите данные через запятую (Каучук, Сера, Сульфенамид, Белила, Стеариновая кислота, Замедлитель, Битум, Пластификатор, Противостаритель, Защитный воск, Техуглерод): ")
    
    preds = model.predict([[1.3908,0.018,0.0369,0.03959,0.01944,0.006,0.05307,0.22463999999999998,0.006840000000000001,0.00972,0.67872]])
    print(preds)