def x_pow (x, y):
    try:
        res = x ** y
    except TypeError:
        return "Введите положительное число и отрицательное"
    return res

print(x_pow(56, -8))

