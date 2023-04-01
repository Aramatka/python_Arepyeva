'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5'''

list_1 = list()
for i in range(int(input('Введите колличество элементов массива: '))):
   m = int(input())
   list_1.append(m) 

print (list_1)

X = int(input('Введите число Х: '))


interval = abs(X - list_1[0])
number = list_1[0]

for i in range(1, len(list_1)):
    if interval > abs(list_1[i] - X):
        interval = abs(list_1[i] - X)
        number = list_1[i]
        
print(number)