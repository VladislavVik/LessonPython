# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('введите секунды:'))
houre = time // 3600
minetes = (time - houre * 3600) // 60
seconds = time - 60 * minetes - houre * 3600
#print('часы:', houre)
#print('минуты:', minetes)
#print('секунды:', seconds)
print('Время в ч:м:с =',houre,':',minetes,':',seconds)