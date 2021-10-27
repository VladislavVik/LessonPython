my_list = input("Напишите числа через пробел: ").split()

for i in range(1, len(my_list), 2):
    my_list.insert(i - 1, my_list.pop(i))

print (my_list)