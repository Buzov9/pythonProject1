import os
from queue import Queue

# print(os.getcwd())#текущая директория
#
# if os.path.exists('new_file'): #True, если такая директория существуе
#     os.chdir('new_file')#изменяет
# else:
#     os.mkdir('new_file')#создает
#     os.chdir('new_file')
# print(os.getcwd())
# # os.makedirs(r'new_file\in_file')#создание директории с определенным уровнем вложенности
# print(os.listdir())
# for i in os.walk('.'):
#     print(i)
# print(chr('A'))


# class MyThread(threading.Thread):
#     def __init__(self, name, counter, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#
#     def timer(self, name, counter, delay):
#         while counter:
#             time.sleep(delay)
#             print(f'{name} {time.ctime(time.time())}')
#             counter -= 1
#
#
#     def run(self):
#         print(f"поток {self.name} запущен")
#         self.timer(self.name, self.counter, self.delay)
#         print(f"поток {self.name} завершен")

q = queue = Queue()
q.put(12)
print(q.get())