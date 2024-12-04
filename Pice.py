from threading import Thread, Event
from time import sleep
import multiprocessing



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

counter = 0


def first(n):
    global counter
    for i in range(n):
        counter += 1
        sleep(0.5)
        print(' 1w!', counter)

    print('exelent 1w!', counter)


def second(n):
    global counter
    for i in range(n):
        counter += 1
        sleep(0.5)
        print(' 2w!', counter)

    print('exelent! 2w', counter)


if __name__ == '__main__':
    pr1 = multiprocessing.Process(target=first, args=(10, ))
    pr2 = multiprocessing.Process(target=second, args=(10,))
    pr1.start()
    pr2.start()
