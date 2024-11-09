def is_prime(func):
    def wrapper(*num):
        sum_ = func(*num)
        div = (sum_ % x == 0 for x in range(2, sum_))
        if any(div):
            return f"Составное \n{sum_}"
        else:
            return f"Простое \n{sum_}"
    return wrapper


@is_prime
def sum_three(*nums):
    return sum(nums)


result = sum_three(2, 3, 6)
print(result)