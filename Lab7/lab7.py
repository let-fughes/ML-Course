import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

try:
    matplotlib.use('TkAgg')
except Exception:
    pass

plt.style.use('seaborn-v0_8-whitegrid')

df = pd.read_csv('kaggle_Interests_group.csv')

data = df.drop(['group'], axis=1)

data = data.fillna(0)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

inertia = []
k_range = range(2, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(k_range, inertia, 'bo-')
plt.xlabel('Количество кластеров (k)')
plt.ylabel('Инерция')
plt.title('Метод локтя для K-Means')
plt.show()

OPTIMAL_K = 5

models = {
    "K-Means": KMeans(n_clusters=OPTIMAL_K, random_state=42, n_init=10),
    "DBSCAN": DBSCAN(eps=0.5, min_samples=5),
    "Hierarchical": AgglomerativeClustering(n_clusters=OPTIMAL_K)
}

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for ax, (name, model) in zip(axes, models.items()):
    labels = model.fit_predict(data_scaled)

    if len(np.unique(labels)) > 1:
        score = silhouette_score(data_scaled, labels)
        print(f"{name} Silhouette Score: {score:.4f}")

    sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=labels,
                    palette='viridis', ax=ax, s=50, legend='full')
    ax.set_title(f'Кластеризация: {name}')
    ax.set_xlabel('PCA 1')
    ax.set_ylabel('PCA 2')

plt.tight_layout()
plt.show()