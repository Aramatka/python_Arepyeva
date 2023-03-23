'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |'''

print ('Приветствую! Введите трёхзначное число: ')
number = int(input ())
sumnumber = 0
while number>0:
    sumnumber = sumnumber+number%10
    number = int(number/10)
print (sumnumber)
