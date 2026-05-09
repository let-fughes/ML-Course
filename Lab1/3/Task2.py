class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


manager = Position("Иван", "Петров", "Менеджер", 50000, 15000)
dev = Position("Анна", "Сидорова", "Разработчик", 120000, 30000)

print(f"Сотрудник: {manager.get_full_name()}")
print(f"Должность: {manager.position}")
print(f"Полный доход: {manager.get_total_income()} руб.")

print("-" * 20)

print(f"Сотрудник: {dev.get_full_name()}")
print(f"Должность: {dev.position}")
print(f"Полный доход: {dev.get_total_income()} руб.")