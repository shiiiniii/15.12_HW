# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

num1 = int(input('Введите координаты точки X: '))
num2 = int(input('Введите координаты точки Y: '))

if num1 < 0 and num2 > 0:
    print('Ваша точка находится в I четверти')
if num1 > 0 and num2 > 0:
    print('Ваша точка находится в II четверти')
if num1 > 0 and num2 < 0:
    print('Ваша точка находится в III четверти')
if num1 < 0 and num2 < 0:
    print('Ваша точка находится в IV четверти')

