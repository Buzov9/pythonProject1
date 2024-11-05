import os
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

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if step <= 0:
            raise StepValueError('Шаг не может быть равен или меньше 0')
        self.pointer = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer > self.stop:
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


# Пример использования
iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
