
def is_prime(func):
    def wrapper(*nums):
        n = True
        res_func = func(*nums)
        for i in range(2, res_func):
            if res_func % i == 0:
                n = False
        if n:
             print('Число  простое')
        else:
            print('Число  составное')
        return res_func
    return wrapper

@is_prime
def sum_three(x, y, z):
    res = x + y + z
    return res



result = sum_three(2, 3, 6)
print(result)