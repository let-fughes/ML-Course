text = input("Введите текст: ").split()
result = [word for word in text if not word.lower().endswith(('а', 'a'))]
print("Результат:", " ".join(result))