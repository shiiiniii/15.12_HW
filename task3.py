# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

num = int(input('Введите номер четверти: '))

if num == 1:
    print('Диапазон возможных координат точек в этой четверти: x < 0 и y > 0')
if num == 2:
    print('Диапазон возможных координат точек в этой четверти: x > 0 и y > 0')
if num == 3:
    print('Диапазон возможных координат точек в этой четверти: x > 0 и y < 0')
if num == 4:
    print('Диапазон возможных координат точек в этой четверти: x < 0 и y < 0')
