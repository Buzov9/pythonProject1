class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:


    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        if not isinstance(__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not 1000000 <= __vin and 9999999 >= __vin:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        self.__numbers = __numbers
        if not isinstance(__numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        elif not len(__numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')



    def __is_valid_vin(self, vin__number):
        if not isinstance(vin__number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not 1000000 <= vin__number and 9999999 >= vin__number:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True


    def __is_valid_number(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        elif not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')