'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no'''
print ('Введите n: ')
n = int(input ())
print ('Введите m: ')
m = int(input ())
print ('Введите количество долек - k: ')
k = int(input ())

chocolate = (k%n == 0 or k%m == 0) and k>0 and k<=n*m
if chocolate == 0:
    print('no')
else:
    print('yes')