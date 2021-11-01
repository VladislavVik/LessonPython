my_string = input('Напишите строку из слов, разделенных пробелами: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i}. {word[:10]}')