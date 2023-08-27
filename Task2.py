'''
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
'''
n = int(input('Введите количество элементов в списке: '))
list = []
for i in range(n):
    a = int(input(f'Введите число {i + 1}: '))
    list.append(a)
print(list)
x = int(input('Введите число: '))
minim = x - list[0]
index = 0
for i in range(len(list)):
    count = x - list[i]
    if count < 0:
        count *= -1
    if count < minim:
        minim = count
        index = i
print(f'Число {list[index]} наиболее близко по величине к числу {x}, их разница составляет {int(x- list[index])}')   

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)