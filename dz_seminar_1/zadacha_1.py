# Найдите сумму цифр трехзначного числа.

a = int(input('Введите трехзначное число: '))
thirdDigit = a % 10
a = a // 10
secondDigit = a % 10
firstDigit = a // 10

print(firstDigit  + secondDigit + thirdDigit)
