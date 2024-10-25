def personal_sum(*numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        for j in range(len(i)):
            try:
                result += i[j]
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i[j]}')
    return result, incorrect_data


def calculate_average(*numbers):
    num_sum = []
    count = 0
    if isinstance(numbers, (list, tuple, str)):
        for i in numbers:
            if isinstance(i, (int, float)):
                try:
                    num_sum.append(i)
                    if isinstance(i, (int, float)):
                        count += 1
                except TypeError:
                    print(f'в numbers записан некорректный тип данных {i}')
            else:
                for j in i:
                    if isinstance(j, (int, float, str)):
                        try:
                            num_sum.append(j)
                            if isinstance(j, (int, float)):
                                count += 1
                        except TypeError:
                            print(f'в numbers записан некорректный тип данных {i}')
    try:
        if count == 1:
            print("В numbers записан некорректный тип данных")
        else:
            return personal_sum(tuple(num_sum))[0]/count
    except ZeroDivisionError:
        print("В numbers записан некорректный тип данных")


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
