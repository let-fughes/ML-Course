import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler

try:
    matplotlib.use('TkAgg')
except Exception:
    pass

plt.style.use('seaborn-v0_8-whitegrid')

X, y = make_regression(n_samples=500, n_features=3, noise=15.0, random_state=42)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_b = np.c_[np.ones((X_scaled.shape[0], 1)), X_scaled]


def compute_mse(X, y, w):
    return np.mean((X.dot(w) - y) ** 2)

def gradient_descent(X, y, learning_rate=0.01, epochs=1000, epsilon=1e-6):
    m, n = X.shape
    np.random.seed(42)
    w = np.random.randn(n)
    mse_history = []

    for _ in range(epochs):
        predictions = X.dot(w)
        errors = predictions - y
        gradients = (2 / m) * X.T.dot(errors)

        w_new = w - learning_rate * gradients
        mse_history.append(compute_mse(X, y, w_new))

        if np.linalg.norm(w_new - w) < epsilon:
            w = w_new
            break
        w = w_new

    return w, mse_history

def stochastic_gradient_descent(X, y, learning_rate=0.01, epochs=1000, epsilon=1e-6):
    m, n = X.shape
    np.random.seed(42)
    w = np.random.randn(n)
    mse_history = []

    for _ in range(epochs):
        random_index = np.random.randint(m)
        xi = X[random_index:random_index + 1]
        yi = y[random_index:random_index + 1]

        prediction = xi.dot(w)
        error = prediction - yi
        gradients = 2 * xi.T.dot(error)

        w_new = w - learning_rate * gradients.flatten()
        mse_history.append(compute_mse(X, y, w_new))

        if np.linalg.norm(w_new - w) < epsilon:
            w = w_new
            break
        w = w_new

    return w, mse_history


w_gd, mse_gd = gradient_descent(X_b, y, learning_rate=0.01, epochs=200)
w_sgd, mse_sgd = stochastic_gradient_descent(X_b, y, learning_rate=0.005, epochs=200)

plt.figure(figsize=(10, 6))
plt.plot(mse_gd, label='Полный GD', linewidth=2)
plt.plot(mse_sgd, label='Стохастический SGD', alpha=0.7)
plt.title('Сравнение сходимости: GD против SGD')
plt.xlabel('Итерации (Эпохи)')
plt.ylabel('MSE')
plt.legend()
plt.show()

def regularized_gd(X, y, reg_type='l2', alpha=0.1, learning_rate=0.001, epochs=500):
    m, n = X.shape
    w = np.zeros(n)

    for _ in range(epochs):
        predictions = X.dot(w)
        errors = predictions - y
        gradients = (2 / m) * X.T.dot(errors)

        if reg_type == 'l2':
            reg_term = 2 * alpha * w
        elif reg_type == 'l1':
            reg_term = alpha * np.sign(w)

        reg_term[0] = 0
        gradients += reg_term
        w -= learning_rate * gradients
    return w


alphas = np.logspace(-3, 3, 20)
weights_l1, weights_l2 = [], []

for a in alphas:
    weights_l1.append(regularized_gd(X_b, y, reg_type='l1', alpha=a, learning_rate=0.001))
    weights_l2.append(regularized_gd(X_b, y, reg_type='l2', alpha=a, learning_rate=0.001))

weights_l1 = np.array(weights_l1)[:, 1:]
weights_l2 = np.array(weights_l2)[:, 1:]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(alphas, weights_l1)
ax1.set_xscale('log')
ax1.set_title('L1 Регуляризация (Нечетный вариант)')
ax1.set_xlabel('Коэффициент alpha')
ax1.set_ylabel('Значения весов')

ax2.plot(alphas, weights_l2)
ax2.set_xscale('log')
ax2.set_title('L2 Регуляризация (Четный вариант)')
ax2.set_xlabel('Коэффициент alpha')
ax2.set_ylabel('Значения весов')

plt.show()