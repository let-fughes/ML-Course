# [Состав, Цена, Количество]
jewelry_store = {
    "Кольцо": ["Золото", 5000, 10],
    "Серьги": ["Серебро", 2500, 5],
    "Браслет": ["Платина", 12000, 3]
}

while True:
    print("\n--- Меню ---")
    print("1. Просмотр описания\n2. Просмотр цены\n3. Просмотр количества")
    print("4. Вся информация\n5. Покупка\n6. До свидания")

    choice = input("Выберите пункт: ")

    if choice == '1':
        for name, info in jewelry_store.items():
            print(f"{name} — {info[0]}")
    elif choice == '2':
        for name, info in jewelry_store.items():
            print(f"{name} — {info[1]} руб.")
    elif choice == '3':
        for name, info in jewelry_store.items():
            print(f"{name} — {info[2]} шт.")
    elif choice == '4':
        for name, info in jewelry_store.items():
            print(f"{name}: состав - {info[0]}, цена - {info[1]}, кол-во - {info[2]}")
    elif choice == '5':
        total_cost = 0
        while True:
            item = input("Введите название изделия (или 'n' для выхода): ")
            if item.lower() == 'n': break

            if item in jewelry_store:
                qty = int(input(f"Сколько {item} хотите купить? "))
                if qty <= jewelry_store[item][2]:
                    jewelry_store[item][2] -= qty
                    total_cost += qty * jewelry_store[item][1]
                    print("Товар добавлен в корзину.")
                else:
                    print("Недостаточно товара на складе!")
            else:
                print("Такого изделия нет.")
        print(f"Итоговая стоимость: {total_cost} руб.")
    elif choice == '6':
        print("До свидания!")
        break