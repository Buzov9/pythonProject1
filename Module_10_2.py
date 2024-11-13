import threading
import time
from tqdm import tqdm


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        while enemy:
            """for i in tqdm(range(10), desc="проходит день"):
                time.sleep(0.1)"""
            time.sleep(1)
            day += 1
            enemy -= self.power
            print(f'{self.name} сражается {day} дней, осталось {enemy} воинов')
        print(f'{self.name} одержал победу спустя {day} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
print('все битвы закончились')