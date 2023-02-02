# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

try:
    numberTicket = int(input('Введите номер билета из шести чисел '))

    f = numberTicket // 1000
    s = numberTicket % 1000

    firstDigit = f // 100
    secondDigit = (f // 10) % 10
    thirdDigit = f % 10
    sum1 = firstDigit + secondDigit + thirdDigit
    fourthDigit = s // 100
    fifthDigit = (s // 10) % 10
    sixthDigit = s % 10
    sum2 = fourthDigit + fifthDigit + sixthDigit

    if(sum1 == sum2):
        print("Поздравляем, у вас счастливый билет!")
    else:
        print("Не повезло")
except:
    print("Вы ввели некорректные данные")

