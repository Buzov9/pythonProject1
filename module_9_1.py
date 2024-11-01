def apply_al_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_al_func([6, 20, 15, 9],  max, min))
print(apply_al_func([6, 20, 15, 9], len, sum, sorted))