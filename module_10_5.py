import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for n, line in enumerate(file, 1):
            all_data.append(file.readline())


files_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    with multiprocessing.Pool(5) as pool:
        start = time.time()
        result = pool.map(read_info, files_list)
        end_time = time.time()
        print('выполнено за: ', end_time - start, 'многопроцессный')

    start_ = time.time()
    map(read_info, filenames)
    end_time_ = time.time()
    print('выполнено за: ', end_time_ - start_, 'линейный')
