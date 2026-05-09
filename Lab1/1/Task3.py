n = int(input("Введите количество чисел (n >= 2): "))
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(n)]

sums = [numbers[i] + numbers[i+1] for i in range(len(numbers) - 1)]
print("Список сумм соседних чисел:", sums)