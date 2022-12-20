import numpy
import random
from alive_progress import alive_bar

# Входящие данные на одну заправку (кг), идеальные пропорции
# 0       1     2            3       4                    5            6      7              8                 9              10   
# Каучук, Сера, Сульфенамид, Белила, Стеариновая кислота, Замедлитель, Битум, Пластификатор, Противостаритель, Защитный воск, Техуглерод
idealInput = [1.22, 0.018, 0.03, 0.037, 0.024, 0.006, 0.061, 0.208, 0.006, 0.012, 0.672]

# Влияние ингридиентов на значения стр 9

# Параметры (индексы) влияющие на твердость
# Техуглерод (стр 28), воск (стр 94),
hardnessParams = [10, 9] 

# Параметры (индексы) влияющие на прочность
# Пластификатор (стр 35)
enduranceParams = [7, 1, 6]

# Параметры (индексы) влияющие на удлиннение
lengthParams = [0, 4, 3, 2]

# Выходные данные, идеальные
hardness = [50, 70]
endurance = 8
length = 200


def GenerateInput():
    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Клонируем массив
    newInput = idealInput.copy()
    
    # Получаем количество параметров для редактирования
    count = random.randint(0, 10)
    
    # Перемешиваем все элементы
    random.shuffle(indexes)
    
    for i in range(count):
        # Индекс, по которому будем менять значение (параметр)
        index = indexes[i]
        
        # Идеальное значение
        idealValue = idealInput[index]
        
        # генерируем процент, на который будет различаться значение
        percentage = round(random.uniform(0.01, 0.25), 2)
        
        # Вычисляем значение по проценту
        percentageAvg = idealValue * percentage

        # Прибавить или уменьшить процент
        posChoice = random.choice([0, 1])
        
        # Вычисляем новое значение
        if posChoice == 1:
            newInput[index] = idealValue + percentageAvg
        else:
            newInput[index] = idealValue - percentageAvg
    return newInput

def GenerateOutput(newInput):
    output = []
    # Идеальный параметр находится в диапазоне
    newhardness = random.randint(hardness[0], hardness[1])
    
    # Составляем идеальные выходные данные
    output.append(newhardness)
    output.append(endurance)
    output.append(length)
    
    for i in range(len(newInput)):
        if idealInput[i] != newInput[i]:
            # Находим на сколько различается параметр
            if newInput[i] > idealInput[i]:
                percentage = (newInput[i] - idealInput[i])
            else:
                percentage = (idealInput[i] - newInput[i])
            
            # Вычисляем процент различия с процентом входного параметра (от 2% до 15%)
            diffPercentage = random.uniform(0.02, 0.15)
            newPercentage = percentage + diffPercentage
              
            # Влияет на твердость
            if i in hardnessParams:
                # Если ингридиентов больше, то свойства увеличиваются, иначе слабеют
                if newInput[i] > idealInput[i]:
                    output[0] = output[0] + output[0] * newPercentage
                else:
                    output[0] = output[0] - output[0] * newPercentage
            
            # Влияет на прочность
            if i in enduranceParams:
                # Если ингридиентов больше, то свойства увеличиваются, иначе слабеют
                if newInput[i] > idealInput[i]:
                    output[1] = output[1] + output[1] * newPercentage
                else:
                    output[1] = output[1] - output[1] * newPercentage
            
            # Влияет на удлиннение
            if i in lengthParams:
                 # Если ингридиентов больше, то свойства увеличиваются, иначе слабеют
                if newInput[i] > idealInput[i]:
                    output[2] = output[2] + output[2] * newPercentage
                else:
                    output[2] = output[2] - output[2] * newPercentage
    return output
    
if __name__ == "__main__":
    # Сгенерируем датасет из 500к входных и выходных данных
    count = 500000
    print(f'Начинаем генерирование датасета, генерируем {count} данных')
    with open('data/dataset.csv', 'w') as f:
        with alive_bar(count) as bar:
            for _ in range(count):
                inp = GenerateInput()
                output = GenerateOutput(inp)
                data = inp + output
                outputData = ','.join([str(n) for n in data])
                f.write(f"{outputData}\n")
                bar()
    print("Генерирование датасета завершено!")