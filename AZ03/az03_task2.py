import numpy as np
import matplotlib.pyplot as plt

# Для воспроизводимости (необязательно)
np.random.seed(0)

# Генерация двух наборов случайных данных (по 5 точек каждый)
x = np.random.rand(5)
y = np.random.rand(5)

# Вывод сгенерированных массивов
print("x:", x)
print("y:", y)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
