# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#   Для решения используйте цикл while и арифметические операции.
natural = int(input('введите число:'))
max_digit = 0
while natural > 0:
    digit = natural % 10
    if digit > max_digit:
        max_digit = digit
    natural = natural // 10
    #print('naturl', natural, 'digit', digit, 'max_digit', max_digit)
print('самая большая цифра в числе:',max_digit)
