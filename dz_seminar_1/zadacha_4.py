# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите размер n: '))
m = int(input('Введите размер m: '))
k = int(input('Введите кол-во долек: '))

if n*m > k and (k % n == 0 or k % m == 0):
    print('Да, можно')
else:
    print('Нет, нельзя')
