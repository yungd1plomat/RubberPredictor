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
    
    preds = model.predict([[1.22,0.018,0.03,0.037,0.024,0.006,0.061,0.208,0.006,0.012,0.672]])
    print(preds)