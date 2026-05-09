word1 = input("Введите первое слово: ").lower().replace(" ", "")
word2 = input("Введите второе слово: ").lower().replace(" ", "")

if sorted(word1) == sorted(word2):
    print("Это анаграммы.")
else:
    print("Это не анаграммы.")