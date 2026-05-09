def process_data(data):
    if isinstance(data, list):
        result = sum(data) / len(data) if data else 0
        print(f"Список. Среднее арифметическое: {result}")

    elif isinstance(data, dict):
        sorted_dict = sorted(data.items(), key=lambda item: item[1])
        print(f"Словарь (отсортирован): {sorted_dict}")

    elif isinstance(data, int):
        s_num = str(data)
        print(f"Число наоборот: {s_num[::-1]}")

    elif isinstance(data, str):
        words = data.split()
        if words:
            longest = max(words, key=len)
            print(f"Строка. Слов: {len(words)}, Самое длинное: '{longest}'")
        else:
            print("Строка пуста")
    else:
        print("Неизвестный тип данных")


process_data([10, 20, 30])
process_data({"a": 10, "b": 5, "c": 20})
process_data(12345)
process_data("Python это замечательный язык программирования")