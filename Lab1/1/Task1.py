number = input("Введите натуральное число: ")
sum_even = sum(int(digit) for digit in number if int(digit) % 2 == 0)
print(f"Сумма четных цифр: {sum_even}")