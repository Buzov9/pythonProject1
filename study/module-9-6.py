def all_variants(text):
    n = len(text)
    var = []
    cuc = 0
    for i in range(n**2):
        if len(var) < n:
            var.append(1)
            cuc += 1
            yield text[i]
        elif len(var) > (n*2)-2:
            yield text
            break
        else:
            var.append(1)
            cuc += 1
            i_in_text = cuc % n
            yield text[i_in_text -1] + text[i_in_text]
# я не понял по какой логике должны выводиться вариации, надеюсь иной смлысл задания я выполнил


a = all_variants('abc')
for i in a:
    print(i)

