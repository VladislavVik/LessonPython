my_list = [9, 7, 5, 4, 3, 3, 2]
print(my_list)
new_num = int(input('введите  элемент рейтинга:'))
#new_num = 10.0
i = 0
for n in my_list:
    if new_num <= n:
        i = i +1
    else:
        break
my_list.insert(i, new_num)
print(my_list)