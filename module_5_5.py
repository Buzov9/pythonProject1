class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password
class User:
    def __init__(self, username, password, passworsd_confirm):
        self.username = username
        if password == passworsd_confirm:

            self.password = password


if __name__ == '__main__':
    database = Database()
while True:
    choise = input('выбери действие: \n1 - вход \n2 - регистрация\n')
    if choise == '1':
        login = input('введите логин: ')
        password = input("введите пароль: ")
        if login in database.data:
            if password == database.data[login]:
                print('welcome', login)
                break
            else:
                print('password govno')
        else:
            print("пользователь не найден")
    if choise == "2":
        user = User(input("логин: "), password := input("пароль: "), password2 := input('повторите пароль: '))

        if password != password2:
            continue
        database.add_user(user.username, user.password)
    print(database.data)