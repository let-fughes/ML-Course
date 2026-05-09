import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from IPython.display import display

sns.set_theme(style="whitegrid")

df = pd.read_csv('train.csv')

print("Размерность данных:", df.shape)
display(df.head())


plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Матрица пропусков (желтым цветом показаны пропущенные значения)')
plt.show()

print("\nКоличество пропусков по признакам:")
print(df.isnull().sum()[df.isnull().sum() > 0])

median_life_sq_ratio = (df['LifeSquare'] / df['Square']).median()
df['LifeSquare'] = df['LifeSquare'].fillna(df['Square'] * median_life_sq_ratio)

df['Healthcare_1'] = df['Healthcare_1'].fillna(df['Healthcare_1'].median())

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Square', 'LifeSquare', 'KitchenSquare']])
plt.title('Распределение площадей (ДО устранения выбросов)')
plt.show()

df.loc[df['Square'] < 10, 'Square'] = df['Square'].median()
df.loc[df['Square'] > 300, 'Square'] = df['Square'].median()

df.loc[df['LifeSquare'] > df['Square'], 'LifeSquare'] = df['Square']

df.loc[df['KitchenSquare'] > df['Square'], 'KitchenSquare'] = df['KitchenSquare'].median()

current_year = 2024
df.loc[(df['HouseYear'] > current_year) | (df['HouseYear'] < 1900), 'HouseYear'] = df['HouseYear'].median()

df.loc[df['Floor'] == 0, 'Floor'] = 1
df.loc[df['HouseFloor'] == 0, 'HouseFloor'] = df['Floor']
df.loc[df['Floor'] > df['HouseFloor'], 'HouseFloor'] = df['Floor']

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Square', 'LifeSquare']])
plt.title('Распределение площадей (ПОСЛЕ устранения выбросов)')
plt.show()

df['LifeToSquareRatio'] = df['LifeSquare'] / df['Square']

df['IsFirstFloor'] = (df['Floor'] == 1).astype(int)
df['IsLastFloor'] = (df['Floor'] == df['HouseFloor']).astype(int)

cat_features = ['Ecology_2', 'Ecology_3', 'Shops_2']
df = pd.get_dummies(df, columns=cat_features, drop_first=True)

for col in df.columns:
    if df[col].dtype == bool:
        df[col] = df[col].astype(int)

num_features = ['Rooms', 'Square', 'LifeSquare', 'KitchenSquare', 'Floor', 'HouseFloor', 'HouseYear', 'Healthcare_1', 'Social_1', 'Social_2', 'Social_3', 'Ecology_1']

scaler = StandardScaler()

df[num_features] = scaler.fit_transform(df[num_features])

print("\nФинальный вид данных после стандартизации:")
display(df.head())