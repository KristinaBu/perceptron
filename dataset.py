import numpy as np
import csv

# Замените 'your_file.csv' на фактическое имя вашего CSV файла
with open('powerconsumption.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Пропускаем заголовок, если он есть
    next(reader, None)  
    data = list(reader)

# Преобразование списка списков в NumPy массив
data = np.array(data, dtype=str)  # Измените dtype на подходящий тип данных


# Получение формы массива
print(data.shape)

# Доступ к элементам массива
print(data[0, 0])  # Первый элемент второй колонки