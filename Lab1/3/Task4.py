class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount}. Новый баланс {self.owner}: {self.balance}")

    @classmethod
    def set_interest_rate(cls, new_rate: float):
        cls.interest_rate = new_rate
        print(f"Глобальная процентная ставка изменена на {new_rate * 100}%")

    @staticmethod
    def is_amount_valid(amount: float) -> bool:
        return amount > 0

my_account = BankAccount("Кирилл", 1000)

amount_to_add = 500
if BankAccount.is_amount_valid(amount_to_add):
    my_account.deposit(amount_to_add)

BankAccount.set_interest_rate(0.07)