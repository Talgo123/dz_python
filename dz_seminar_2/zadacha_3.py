# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число "))
i = 0
res = 0
while (res < n):
    if (2 ** i > n):
        break
    else:
        res = 2 ** i 
        i+=1
    print(res)