from tqdm import tqdm
from time import sleep


class User:
    age = {}
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        password = hash(password)
        self.age = age
        User.age[nickname] = self.age
        UrTube.users.append({nickname: password})


class Video:
    title = []
    duration = {}
    adult = {}
    def __init__(self, title, duration, timeout=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.timeout = timeout
        self.adult_mode = adult_mode
        Video.title.append(title)
        Video.duration[title] = duration
        Video.adult[title] = adult_mode


class UrTube:
    current_user = None

    users = []
    videos = []

    def __init__(self):
        self = []

    def log_in(nickname, password):
        for user in UrTube.users:
            if user[nickname] == hash(password):
                UrTube.current_user = nickname
                print(f'{nickname} вошел')
                return
        print(f'пользователь {nickname} не найден')

    def register (self, nickname, password, age):
        for user in UrTube.users:
            if nickname in user:
                print(f'пользватель {nickname} уже существует')
                return

        new_user = User(nickname, password, age)
        UrTube.current_user = nickname
        print('пользователь успешно зарегестрирован')
        return new_user

    def log_out(self=1):
        UrTube.current_user = None

    def add(self, *new_videos):
        uniqiue_titles = set()
        for video in new_videos:
            if video.title not in uniqiue_titles:
                UrTube.videos.append(video.title)
                uniqiue_titles.add(video.title)

    def get_videos(self, word):
        for i in UrTube.videos:
            if word.lower() in i.lower():
                print(i)


    def watch_video(self, title):
        if title in Video.title:
            if UrTube.current_user == None:
                print('вы не вошли в аккаунт')
            else:
                if Video.adult[title] == True:
                    if User.age[UrTube.current_user] <= 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for i in tqdm(range(Video.duration[title])):
                            sleep(1)#надеюсь так можно о_о



if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
