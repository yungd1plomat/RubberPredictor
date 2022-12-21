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
    inputArray = np.array(np.fromstring(inp, dtype=float, sep=','))
    X = np.array([inputArray])
    preds = model.predict(X)
    print(preds)