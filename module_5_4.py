print(int.__mro__)
class User:
    def __init__(self, *args, **kwargs):
        print('hi')
        self.args = args
        for key, varues in kwargs.items():
            setattr(self, key, varues)


other = [1, 2, 3]
user = {'name':'Den', 'age': 25, 'gender':'male'}

user1 = User(*other, **user)
print(user1.args)
print(user1.name)