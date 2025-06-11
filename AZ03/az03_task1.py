import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0        # Среднее значение
std_dev = 1     # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Для воспроизводимости (необязательно)
np.random.seed(0)

# Генерация случайных данных
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы (без отображения)
plt.hist(data, bins=30)
plt.title('Гистограмма нормального распределения (μ=0, σ=1)')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()
