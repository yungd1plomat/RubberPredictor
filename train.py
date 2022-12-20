import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from LSTM_model import LSTM_Model
from MLP_model import MLP_Model
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
import os

# Путь сохранения моделей
lstmPath = 'models/lstm.model'
mlpPath = 'models/mlp.model'
checkpoint_filepath = 'tmp/cp-{epoch:04d}.h5'


# Количество эпох для обучения
EPOCHS = 200
# Количество обучающих примеров на итерацию
BS = 128

def build_model(model_choose):
    if model_choose == "1" and os.path.isfile(lstmPath):
        model = load_model(lstmPath)
        return model
    elif os.path.isfile(mlpPath):
        model = load_model(mlpPath)
        return model
    if model_choose == "1":
        model = LSTM_Model.build()
        return model
    else:
        model = MLP_Model.build()
        return model

def load_dataset():
    dataset = np.loadtxt("data/dataset.csv", delimiter=",")
    X = dataset[:,0:11]
    Y = dataset[:,11:14] 
    return train_test_split(X, Y, random_state=104, test_size=0.25, shuffle=True)

def show_results(H, model_choose):
    N = np.arange(0, EPOCHS)
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(N, H.history["loss"], label="train_loss")
    plt.plot(N, H.history["val_loss"], label="val_loss")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    if model_choose == "1":
        plt.savefig("lstm")
    else:
        plt.savefig("mlp")

def save_model(model, model_choose):
    if model_choose == "1":
        model.save(lstmPath, save_format="h5")
    else:
        model.save(mlpPath, save_format="h5")

if __name__ == "__main__":
    # Загружаем датасет
    print("[INFO] loading datasets...")
    (trainX, testX, trainY, testY) = load_dataset()

    # Компилируем модель
    print("[INFO] compiling model...")
    model_choose = input("Выберите модель для обучения (1 - LSTM, 2 - MLP): ")
    model = build_model(model_choose)
    model.compile(optimizer="adam", loss="mae", metrics=["accuracy"])

    # Обучаем модель
    print("[INFO] training network...")
    model_checkpoint_callback = ModelCheckpoint(
        filepath=checkpoint_filepath,
        verbose=1, 
        save_weights_only=False,
        save_freq='epoch')
    
    H = model.fit(trainX, trainY, epochs=EPOCHS, batch_size=BS, validation_data=(testX, testY), callbacks=[model_checkpoint_callback])

    # Тестируем модель
    print("[INFO] evaluating model..")
    predictions = model.predict(testX, batch_size=BS)
    print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1)))

    # Сохраняем
    print("[INFO] saving model...")
    save_model(model, model_choose)

    # Отображаем график обучения
    show_results(H, model_choose)

    print("[INFO] FINISHED!")
