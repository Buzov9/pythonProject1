def all_variants(text):

    n = len(text)
    for i in range(1, 2**n):
        var_list = ''
        for j in range(n):
            if (i >> j) & 1:
                var_list += text[j]
        yield var_list
# я не понял по какой логике должны выводиться вариации, надеюсь иной смлысл задания я выполнил


a = all_variants('abc')
for i in a:
    print(i)