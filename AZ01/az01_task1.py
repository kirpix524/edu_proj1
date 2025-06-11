import pandas as pd

df = pd.read_csv("../data/Citywide_Payroll_Data__Fiscal_Year_.csv")

print(df.head())
print(df.info())
print(df.describe())
