team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
print('В команде Мастера кода участников: %(num)s' %{'num': team1_num})
team2_num = 6
print('Итого сегодня в командах участников: %(team)s и %(team2)s' %{'team': team1_num, 'team2': team2_num})
score_2 = 21
print("Команда Волшебники данных решила задач:{title}!".format(title=score_2) )
team2_time = 9900.1
score_1 = 25
team1_time = 1323.3
print('Волшебники данных решили задачи за {title}'.format(title=team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
tasks_total = score_2 + score_1
time_avg = (team1_time + team2_time)/(score_1 + score_2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result
print(f'Результат битвы: победа команды {challenge_result}!')
