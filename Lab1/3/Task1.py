class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0

    def input_data(self):
        try:
            self.a = float(input("Введите первое число: "))
            self.b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно вводить числа!")
            return False
        return True

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Ошибка: деление на ноль!"
        return self.a / self.b

calc = Calculator()
if calc.input_data():
    print(f"Сумма: {calc.add()}")
    print(f"Разность: {calc.subtract()}")
    print(f"Произведение: {calc.multiply()}")
    print(f"Частное: {calc.divide()}")