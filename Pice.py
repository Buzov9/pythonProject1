# import random
# import time
# from threading import Thread
# import queue
# import logging
#
#
# class Bulka(Thread):
#     def __init__(self, queue):
#         self.queue = queue
#         super().__init__()
#
#     def run(self):
#         while True:
#             time.sleep(random.randint(1,5))
#             if random.randint(1, 100) > 90:
#                 self.queue.put('подгорелая булка')
#             else:
#                 self.queue.put('нормальнаЯ булка')
#
# class Kotleta(Thread):
#
#     def __init__(self, queue, count):
#         self.queue = queue
#         self.count = count
#         super().__init__()
#
#
#     def run(self):
#         while self.count:
#             bulka = self.queue.get()
#             if bulka == 'нормальнаЯ булка':
#                 time.sleep(random.randint(1, 5))
#                 self.count -= 1
#             print('булок к приготовлению осталось', self.count)
#
#
# queue = queue.Queue()
#
# t1 = Bulka(queue)
# t2 = Kotleta(queue, 20)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

file = open('re', 'w')