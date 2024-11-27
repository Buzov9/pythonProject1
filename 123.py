import random
import threading
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(10):
            random_count = random.randint(50, 500)
            with self.lock:
                if self.balance + random_count > 500:
                    pass
                else:
                    self.balance += random_count
                    print(f"Пополнение: {random_count}. Баланс: {self.balance}")
            sleep(0.01)

    def take(self):
        for i in range(10):
            random_count = random.randint(50, 500)
            with self.lock:
                print(f'Запрос на снятие {random_count}. Баланс: {self.balance}')
                if self.balance < random_count:
                    print(f'Недостаточно средств')
                else:
                    self.balance -= random_count
                    print(f'Снятие: {random_count}, текущий баланс: {self.balance}')
            sleep(0.01)


bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
