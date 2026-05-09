def safe_divide():
    try:
        a = int(input("Введите числитель: "))
        b = int(input("Введите знаменатель: "))
        result = a / b
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: На ноль делить нельзя!")
    except ValueError:
        print("Ошибка: Введите именно целое число!")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        print("Завершение работы блока обработки.")

safe_divide()