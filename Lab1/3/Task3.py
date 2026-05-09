class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки для {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Ручка '{self.title}' пишет тонкой линией.")


class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш '{self.title}' рисует эскиз.")


class Handle(Stationery):
    def draw(self):
        print(f"Маркер '{self.title}' выделяет текст жирным цветом.")


if __name__ == "__main__":
    pen = Pen("Parker")
    pencil = Pencil("Koh-i-Noor")
    handle = Handle("Stabilo")

    pen.draw()
    pencil.draw()
    handle.draw()

    base = Stationery("Неизвестный предмет")
    base.draw()