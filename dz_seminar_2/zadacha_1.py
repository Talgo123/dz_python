# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint
n = int(input("Введите кол-во монеток "))

side = []
count1 = 0
count2 = 0
for _ in range(n):
    #side.append(int(input("Введите 1 или 0 ")))
    side.append(randint(0,1))
print(side)

for i in side:
    if i > 0:
        count1+=1
    else:
        count2+=1
if count1 > count2:
    print(count2)
elif count1 == count2:
    print(count1)
else:
    print(count1)
        