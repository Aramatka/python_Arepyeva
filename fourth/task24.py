'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности.
 Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.

Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.'''

n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count=list()
for i in range(len(arr)-1):
    arr_count.append(arr[i-1]+arr[i]+arr[i+1])
arr_count.append(arr[-2]+arr[-1]+arr[0])
print(max(arr_count))