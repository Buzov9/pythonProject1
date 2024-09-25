class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)


h1 = House('ЖК Крылатый', 16)
h2 = House('Общежитие №3', 9)
h1.go_to(12)
h2.go_to(0)