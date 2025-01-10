import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
) 
''')

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ? )", (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

# Меняем баланс:
# for user in users:
#     if user[0] % 2:
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, user[0]))

# #Удаляем каждого 3-его:
# for i, user in enumerate(users):
#     i += 3
#     if not i % 3:
#         cursor.execute("DELETE FROM Users WHERE id = ?", (user[0],))

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')
connection.commit()
connection.close()