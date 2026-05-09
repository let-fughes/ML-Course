# Machine Learning Laboratory Works / Лабораторные работы по Машинному Обучению

This document contains README templates for Laboratory Works 4 to 8.
Этот документ содержит шаблоны README для лабораторных работ с 4 по 8.

---

## Lab 4: Data Classification / ЛР 4: Классификация данных

### English
**Description:**
Implementation of binary classification models to predict bank loan defaults. The project covers data cleaning, outlier removal (IQR), and comparison of Logistic Regression, SVM, and CART models.

**Key Features:**
- Handling class imbalance using `class_weight='balanced'`.
- Evaluation using Precision, Recall, and F1-score.

#### Plots to insert:
1. **Confusion Matrix:** Showing True Positives vs False Negatives.
   `![Confusion Matrix](path_to_image/confusion_matrix_lab4.png)`
2. **Model Metrics Comparison:** Bar chart comparing Accuracy and Recall across models.
   `![Metrics Comparison](path_to_image/metrics_comparison_lab4.png)`

### Русский
**Описание:**
Реализация моделей бинарной классификации для прогнозирования дефолтов по банковским кредитам. Проект включает очистку данных, удаление выбросов (IQR) и сравнение логистической регрессии, SVM и CART.

**Ключевые особенности:**
- Обработка дисбаланса классов с помощью `class_weight='balanced'`.
- Оценка качества через Precision, Recall и F1-score.

#### Места для графиков:
1. **Матрица ошибок:** Показывает соотношение верных и ложных предсказаний.
   `![Матрица ошибок](путь_к_фото/confusion_matrix_lab4.png)`
2. **Сравнение метрик:** Гистограмма точности и полноты для разных моделей.
   `![Сравнение метрик](путь_к_фото/metrics_comparison_lab4.png)`

---

## Lab 5: Decision Trees / ЛР 5: Деревья решений

### English
**Description:**
A "from-scratch" implementation of a Decision Tree classifier. It demonstrates the internal mechanics of recursive splitting based on Gini Impurity and Information Gain.

**Implemented Logic:**
- Gini Index & Information Gain calculation.
- Stopping criteria (max depth, min samples per leaf).
- Accuracy comparison with `sklearn.tree.DecisionTreeClassifier`.

#### Plots to insert:
1. **Tree Structure:** A visualization of the resulting decision tree nodes.
   `![Decision Tree Structure](path_to_image/tree_visualization.png)`
2. **Accuracy Scatter Plot:** Comparison between custom implementation and sklearn.
   `![Accuracy Comparison](path_to_image/accuracy_comparison_lab5.png)`

### Русский
**Описание:**
Реализация классификатора «Дерево решений» с нуля. Демонстрирует внутреннюю механику рекурсивного разбиения на основе критерия Джини и прироста информации.

**Реализованная логика:**
- Расчет индекса Джини и Information Gain.
- Критерии останова (макс. глубина, мин. количество объектов в листе).
- Сравнение точности с `sklearn.tree.DecisionTreeClassifier`.

#### Места для графиков:
1. **Структура дерева:** Визуализация узлов и ветвлений полученного дерева.
   `![Структура дерева](путь_к_фото/tree_visualization.png)`
2. **График точности:** Сравнение результатов самописной модели и библиотеки sklearn.
   `![Сравнение точности](путь_к_фото/accuracy_comparison_lab5.png)`

---

## Lab 6: Model Ensembles / ЛР 6: Ансамбли моделей

### English
**Description:**
Using ensemble methods (Gradient Boosting and Random Forest) to improve prediction stability. Includes automated hyperparameter tuning.

**Workflow:**
- GridSearch optimization for `n_estimators`, `learning_rate`, and `max_depth`.
- Feature importance analysis.

#### Plots to insert:
1. **Feature Importance:** Ranking of input variables by their impact on the model.
   `![Feature Importance](path_to_image/feature_importance_lab6.png)`
2. **Hyperparameter Heatmap:** Results of GridSearchCV for different parameter combinations.
   `![GridSearch Heatmap](path_to_image/gridsearch_results.png)`

### Русский
**Описание:**
Использование ансамблевых методов (градиентный бустинг и случайный лес) для повышения устойчивости прогнозов. Включает автоматизированный подбор гиперпараметров.

**Рабочий процесс:**
- Оптимизация параметров `n_estimators`, `learning_rate` и `max_depth` через GridSearch.
- Анализ важности признаков.

#### Места для графиков:
1. **Важность признаков:** Рейтинг входных переменных по их влиянию на модель.
   `![Важность признаков](путь_к_фото/feature_importance_lab6.png)`
2. **Тепловая карта параметров:** Результаты GridSearchCV для различных комбинаций.
   `![Результаты GridSearch](путь_к_фото/gridsearch_results.png)`

---

## Lab 7: Clustering / ЛР 7: Кластеризация

### English
**Description:**
Unsupervised learning project to group people based on their interests. Compares density-based, centroid-based, and hierarchical approaches.

**Techniques Used:**
- PCA (Principal Component Analysis) for 2D visualization.
- Elbow Method to find the optimal number of clusters.

#### Plots to insert:
1. **Elbow Method Curve:** Plot of inertia vs number of clusters.
   `![Elbow Method](path_to_image/elbow_plot_lab7.png)`
2. **Cluster Visualization (PCA):** 2D scatter plot of user groups.
   `![Cluster Clusters](path_to_image/pca_clusters_lab7.png)`

### Русский
**Описание:**
Проект обучения без учителя для группировки людей на основе их интересов. Сравнение подходов на основе плотности, центроидов и иерархических связей.

**Использованные методы:**
- PCA (метод главных компонент) для 2D визуализации.
- Метод «локтя» для определения оптимального числа кластеров.

#### Места для графиков:
1. **График «локтя»:** Зависимость инерции от количества кластеров.
   `![Метод локтя](путь_к_фото/elbow_plot_lab7.png)`
2. **Визуализация кластеров (PCA):** 2D диаграмма рассеяния групп пользователей.
   `![Визуализация кластеров](путь_к_фото/pca_clusters_lab7.png)`

---

## Lab 8: Convolutional Neural Networks (CNN) / ЛР 8: Сверточные нейронные сети

### English
**Description:**
Deep Learning project for image recognition using the CIFAR-10 dataset. Focuses on architecture design and convolutional filter analysis.

**Architecture:**
- Multiple Conv2D layers with Batch Normalization.
- Dropout layers for regularization.
- Visualization of the learned weights in the first layer.

#### Plots to insert:
1. **Training History:** Loss and Accuracy curves for training and validation sets.
   `![Training History](path_to_image/cnn_training_history.png)`
2. **First Layer Filters:** Visualization of the 32 convolutional filters.
   `![CNN Filters](path_to_image/convolutional_filters.png)`

### Русский
**Описание:**
Проект глубокого обучения для распознавания изображений с использованием набора данных CIFAR-10. Основное внимание уделено архитектуре сети и анализу сверточных фильтров.

**Архитектура:**
- Несколько слоев Conv2D с пакетной нормализацией (Batch Normalization).
- Слои Dropout для регуляризации.
- Визуализация весов, изученных на первом слое.

#### Места для графиков:
1. **История обучения:** Кривые потерь и точности для обучающей и валидационной выборок.
   `![История обучения](путь_к_фото/cnn_training_history.png)`
2. **Фильтры первого слоя:** Визуализация 32-х сверточных фильтров.
   `![Фильтры CNN](путь_к_фото/convolutional_filters.png)`
