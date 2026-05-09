# Machine Learning Course | Лабораторные работы по МO

This repository contains a series of laboratory works focused on data preprocessing, classical machine learning algorithms, and deep learning.
В данном репозитории представлены лабораторные работы, охватывающие этапы предобработки данных, классические алгоритмы машинного обучения и глубокое обучение.

---

## Structure / Структура

### Lab 2: Data Preparation & Cleaning / ЛР 2: Подготовка данных
**English:** Initial data processing: handling missing values, outlier detection using BoxPlots, and feature engineering.
**Русский:** Предварительная обработка данных: анализ пропусков, оценка распределения и поиск выбросов через BoxPlot.
- **Plots / Графики:**
  - `![Missing Values / Heatmap](pics/2.1.png)`
  - `![Data Distribution](pics/2.2.png)`
  - `![Outliers Boxplot](pics/2.3.png)`

### Lab 3: Linear Models / ЛР 3: Линейные модели
**English:** Implementation of Linear Regression and analyzing metric optimization (MSE, R2).
**Русский:** Реализация линейной регрессии и анализ оптимизации метрик (MSE, R2).
- **Plots / Графики:**
  - `![Learning Curve](pics/3.1.png)`
  - `![Regression Analysis](pics/3.2.png)`

### Lab 4: Data Classification / ЛР 4: Классификация данных
**English:** Implementation of binary classification (Logistic Regression, SVM, CART) to predict bank loan defaults.
**Русский:** Реализация бинарной классификации (Логистическая регрессия, SVM, CART) для прогнозирования дефолтов по кредитам.
- **Plots / Графики:**
  - `![Metrics Comparison](pics/4.1.png)`

### Lab 5: Decision Trees / ЛР 5: Деревья решений
**English:** A custom "from-scratch" implementation of a Decision Tree classifier using Gini Impurity.
**Русский:** Самописная реализация классификатора "Дерево решений" на основе критерия Джини.
*(Графики для данной работы не выводились/не сохранялись).*

### Lab 6: Model Ensembles / ЛР 6: Ансамбли моделей
**English:** Advanced prediction using Random Forest and Gradient Boosting with GridSearchCV optimization.
**Русский:** Продвинутое прогнозирование с использованием Random Forest и Gradient Boosting с оптимизацией через GridSearchCV.
- **Plots / Графики:**
  - `![Feature Importance](pics/6.1.png)`
  - `![GridSearch Heatmap](pics/6.2.png)`

### Lab 7: Clustering / ЛР 7: Кластеризация
**English:** Unsupervised learning to group user interests using K-Means and DBSCAN with PCA visualization.
**Русский:** Обучение без учителя: сегментация интересов пользователей с помощью K-Means, DBSCAN и визуализация через PCA.
- **Plots / Графики:**
  - `![Elbow Method](pics/7.1.png)`
  - `![PCA Clusters Map](pics/7.2.png)`

### Lab 8: Convolutional Neural Networks (CNN) / ЛР 8: Сверточные нейросети
**English:** Deep Learning for CIFAR-10 image recognition and visualization of learned convolutional filters.
**Русский:** Глубокое обучение для распознавания изображений CIFAR-10 и визуализация обученных сверточных фильтров.
- **Plots / Графики:**
  - `![Training History Loss/Acc](pics/8.1.png)`
  - `![CIFAR-10 Predictions](pics/8.2.png)`
  - `![Convolutional Filters](pics/8.3.png)`

---

## Setup & Environment / Настройка окружения

**Tested on:** Arch Linux  
**Python:** 3.12 (Recommended for ML stability)  
**Core Stack:** `tensorflow`, `scikit-learn`, `pandas`, `matplotlib`, `seaborn`

```bash
# Clone the repository
git clone [https://github.com/let-fughes/ML-Course.git](https://github.com/let-fughes/ML-Course.git)
cd ML-Course

# Create and activate a virtual environment 
python3.12 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
