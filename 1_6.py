goods = []
features = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'eд': []}
num = 0
while True:
    if input('для выхода нажмите ""q"').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'введите значение свойства "{f}":')
        f_copy[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(f_copy[f])
    goods.append((num, f_copy))
    print(f"\n структура товаров \n {goods}")
    print(f"\n Текущая аналитика по товарам \n {'_' * 30}")
    for key, value in analytics.items():
        print(f'{key:>30}:{value}')
    print('_' * 30)