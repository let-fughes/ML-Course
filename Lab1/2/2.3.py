matrix = [
    [1, 1, 3],
    [4, 5, 6],
    [7, 1, 1]
]

columns = zip(*matrix)
count = 0

for col in columns:
    if all(element != 0 for element in col):
        count += 1

print(f"Количество столбцов без нулей: {count}")