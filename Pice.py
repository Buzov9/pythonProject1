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
sum_ = 11
pop = (sum_ % x == 0 for x in range(2, sum_))
if any(pop):
    print(12)
