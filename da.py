###Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
##a = int(input())
##res = a > 0
##print(res)
###Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
##a = int(input())
##res = a % 2 != 0
##print(res)
### Дано целое число A. Проверить истинность высказывания: «Число A является четным».
##a = int(input())
##res = a %2 == 0
##print(res)
#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3»
##print('введите число В')
##b = int(input())
##print('введите число А')
##a = int(input())
##res = a > 2 and b <= 3
##print(res)
###Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2»
##print('введите А')
##a  = int(input())
##print('введите В')
##b = int(input())
##res = a >= 0 or b < (-2)
##print(res)
#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C».
##print('введите а')
##a = int(input())
##print('vvedite b')
##b = int(input())
##print('vvedite c')
##c = int(input())
##res = a < b < c
##print(res)
### Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C»
##a = int(input())
##b = int(input())
##c = int(input())
##res = b < a and b > c
##print(res)
###Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».
##a = int(input())
##b = int(input())
##res = a % 2 != 0 and b % 2 != 0 
##print(res)
###Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное»
##a = int(input())
##b = int(input())
##res = a % 2 != 0 or b % 2 != 0 
###Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».
##a = int(input())
##b = int(input())
##res = a % 2 != 0 and not b % 2 != 0 or ()
##print(res)
###Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B имеют одинаковую четность».
##a = int(input())
##b = int(input())
##res = (a % 2 != 0 and b % 2 != 0)  or (a % 2 == 0 or b % 2 == 0)
##print(res)
###Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A, B, C положительное».
##a = int(input())
##b = int(input())
##c = int(input())
##res = a > 0 and b >0 and c > 0
##print(res)
###Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно из чисел A, B, C положительное»
##a = int(input())
##b = int(input())
##c = int(input())
##res = a > 0 or b > 0 or c > 0
##print(res)
###Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».
##a = int(input())
##b = int(input())
##c = int(input())
##res = a > 0 and not b > 0 and not c > 0
##print(res)
###Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».
##a = int(input())
##b = int(input())
##c = int(input())
##res = a > 0 and  b > 0 and not c > 0 or a > 0 and not b > 0 and c > 0 or not a > 0 and b > 0 and c > 0
##print(res)
###Дано целое положительное число. Проверить истинность высказывания: «Данное число является четным двузначным»
##print('vvedite polojitelnoe chislo')
##a = int(input())
##res = a % 2 == 0 and a % 10 != 0 or a % 10 == 0
##print(res)
###Дано целое положительное число. Проверить истинность высказывания: «Данное число является нечетным трехзначным».
##print('vvedite polojitelnoe chislo')
##a = int(input())
##res = a % 2 != 0 and a % 100 != 0 or a % 100 == 0
##print(res)
###Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих».
##a = int(input())
##b = int(input())
##c = int(input())
##res = 
##print(res)
###. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного числа различны».
##print('vvedite trexznachnoe chislo')
##a = int(input())
##p = a // 100
##v = a //10 - p * 10
##t = a % 10
##res = p != v and p != t and v != t
##print(res)
### Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа образуют возрастающую последовательность».
##a = int(input())
##p = a // 100
##v = a //10 - p * 10
##t = a % 10
##res = p < v < t
##print(res)
###Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа образуют возрастающую или убывающую последовательность»
##a = int(input())
##p = a // 100
##v = a //10 - p * 10
##t = a % 10
##res = p < v < t or p > v > t
##print(res)
###Дано четырехзначное число. Проверить истинность высказывания: «Данное число читается одинаково слева направо и справа налево».
##a = int(input())
##p = a // 100
##v = a //10 - p * 10
##t = a % 10
##res = p == t
##print(res)
###Даны числа A, B, C (число A не равно 0). Рассмотрев дискриминант D = B 2 − 4·A·C, проверить истинность высказывания: «Квадратное уравнение A·x * x + B·x + C = 0 имеет вещественные корни».
##print('pervoe chislo ne ravno 0')
##a = int(input())
##b = int(input())
##c = int(input())
##D = b * b - 4 * a * c
##res = D >= 0
##print(res)
###Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит во второй координатной четверти».
##print('vvedite x')
##x = int(input())
##print('vvedite y')
##y = int(input())
##res = x < 0 and y > 0
##print(res)
### Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит в четвертой координатной четверти»
##print('vvedite x')
##x = int(input())
##print('vvedite y')
##y = int(input())
##res = y < 0 and x > 0
##print(res)
###Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит во второй или третьей координатной четверти».
##print('vvedite x')
##x = int(input())
##print('vvedite y')
##y = int(input())
##res = x < 0 and y > 0 or x < 0 and y < 0
##print(res)
###Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит в первой или третьей координатной четверти».
##print('vvedite x')
##x = int(input())
##print('vvedite y')
##y = int(input())
##res = x > 0 and y > 0 or x < 0 and y < 0
##print(res)
#Даны числа x, y, x1, y1, x2, y2. Проверить истинность высказывания: «Точка с координатами (x, y) лежит внутри прямоугольника, левая верхняя вершина которого имеет координаты (x1, y1), правая нижняя — (x2, y2), а стороны параллельны координатным осям».

































































