import numpy as np
import pandas as pd

# 1. Генерируем данные
np.random.seed(0)  # для воспроизводимости
students = [f"Ученик_{i+1}" for i in range(10)]
subjects = ['Математика', 'Русский язык', 'Физика', 'История', 'Биология']

# Оценки от 2 до 5 включительно, целые
data = np.random.randint(3, 6, size=(10, 5))

# 2. Создаём DataFrame
df = pd.DataFrame(data, index=students, columns=subjects)

# 3. Выводим первые несколько строк
print("Первые строки DataFrame:")
print(df.head(), end='\n\n')

# 4. Средняя оценка по каждому предмету
mean_per_subject = df.mean()
print("Средние оценки по предметам:")
print(mean_per_subject, end='\n\n')

# 5. Медианная оценка по каждому предмету
median_per_subject = df.median()
print("Медианные оценки по предметам:")
print(median_per_subject, end='\n\n')

# 6. Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"Q1 по математике: {Q1_math}")
print(f"Q3 по математике: {Q3_math}")
print(f"IQR по математике: {IQR_math}", end='\n\n')

# 7. Стандартное отклонение по каждому предмету
std_per_subject = df.std()
print("Стандартное отклонение по предметам:")
print(std_per_subject)
