class WordsFinder:
    file_name = []
    result_of_get_all_words = {}

    def __init__(self, *files):
        self.files = files
        for file in files:
            self.file_name.append(file)

    def get_all_words(self):
        all_words = {}
        line_list = []
        pun = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_name:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line_list += line.lower().split()
            for char in range(len(line_list)):
                for j in pun:
                    new_list = None
                    if j in line_list[char]:
                        new_list = line_list[char][:-1]
                        line_list[char] = new_list
            all_words[i] = line_list
            self.result_of_get_all_words = all_words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for key, value in self.result_of_get_all_words.items():
            for index, (j) in enumerate(value):
                if word == j:
                    result[key] = index + 1
                    break
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        count_ = 0
        for key, value in self.result_of_get_all_words.items():
            for j in value:
                if word == j:
                    count_ += 1
            result[key] = count_
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


