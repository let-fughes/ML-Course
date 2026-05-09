import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.preprocessing import StandardScaler, RobustScaler

try:
    matplotlib.use('TkAgg')
except Exception:
    pass

plt.style.use('seaborn-v0_8-whitegrid')

df = pd.read_csv('train.csv')

print("Пропуски до обработки:\n", df.isnull().sum())

df['Healthcare_1'] = df['Healthcare_1'].fillna(df['Healthcare_1'].median())
df['LifeSquare'] = df['LifeSquare'].fillna(df['Square'] * 0.8)

plt.figure(figsize=(12, 5))
sns.boxplot(data=df[['Square', 'LifeSquare', 'KitchenSquare']])
plt.title('Поиск выбросов в площадях')
plt.show()

df.loc[df['HouseYear'] > 2026, 'HouseYear'] = 2020
df.loc[df['KitchenSquare'] > 100, 'KitchenSquare'] = df['KitchenSquare'].median()
df = df[df['Square'] < 300] # Удаляем экстремально большие объекты

df['Room_Size'] = df['Square'] / df['Rooms'].replace(0, 1)

df['HouseAge'] = 2026 - df['HouseYear']

df = pd.get_dummies(df, columns=['Ecology_2', 'Ecology_3', 'Shops_2'], drop_first=True)

features = ['Rooms', 'Square', 'LifeSquare', 'KitchenSquare', 'Floor',
            'HouseFloor', 'HouseAge', 'Ecology_1', 'Social_1', 'Room_Size']

scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[features] = scaler.fit_transform(df[features])

print("\nДанные после обработки (первые 5 строк):")
print(df_scaled[features].head())

plt.figure(figsize=(12, 10))
sns.heatmap(df[features + ['Price']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Корреляция признаков с ценой')
plt.show()