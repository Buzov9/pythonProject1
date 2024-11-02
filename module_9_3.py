first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = ((len(x) - len(y)) for x, y in zip(first, second) if not len(x) == len(y))
second_result = ((range(len(first[x])) == range(len(second[x]))) for x in range(len(first)))

print(list(first_result))
print(list(second_result))
