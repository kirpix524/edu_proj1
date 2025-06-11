import pandas as pd

df = pd.read_csv("../data/dz.csv")
print(F"Средняя зарплата: {df['Salary'].mean()}")
print(f"Медиана зарплаты: {df['Salary'].median()}")
