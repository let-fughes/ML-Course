import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, utils
from sklearn.metrics import confusion_matrix

try:
    matplotlib.use('TkAgg')
except Exception:
    pass

plt.style.use('seaborn-v0_8-whitegrid')

print("Загрузка данных CIFAR-10...")
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

train_images, test_images = train_images / 255.0, test_images / 255.0

train_labels_cat = utils.to_categorical(train_labels, 10)
test_labels_cat = utils.to_categorical(test_labels, 10)

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    layers.BatchNormalization(),
    layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.2),

    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.3),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.4),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

history = model.fit(train_images, train_labels_cat, epochs=10,
                    validation_data=(test_images, test_labels_cat),
                    batch_size=64)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.title('Точность модели')
plt.legend()

plt.subplot(1, 2, 2)
test_probs = model.predict(test_images)
test_preds = np.argmax(test_probs, axis=1)
cm = confusion_matrix(test_labels, test_preds)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title('Матрица ошибок')
plt.show()

plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i])
    actual = class_names[test_labels[i][0]]
    predicted = class_names[test_preds[i]]
    color = 'green' if actual == predicted else 'red'
    plt.xlabel(f"Actual: {actual}\nPred: {predicted}", color=color)
plt.tight_layout()
plt.show()

filters, biases = model.layers[0].get_weights()
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)

plt.figure(figsize=(8, 8))
for i in range(16):
    f = filters[:, :, :, i]
    plt.subplot(4, 4, i+1)
    plt.imshow(f[:, :, 0], cmap='gray')
    plt.axis('off')
plt.suptitle('Фильтры первого сверточного слоя')
plt.show()