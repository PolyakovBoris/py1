from random import randint

# 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


side_a = 10
side_b = 8
side_c = 9
if (side_a + side_b > side_c) & (side_b + side_c > side_a) & (side_a + side_c > side_b):
    if (side_a == side_b == side_c):
        print('треугольник равносторонний')
    elif (side_a == side_b) | (side_b == side_c) | (side_a == side_c):
        print('треугольник равнобедренный')
    elif (side_a != side_b != side_c):
        print('треугольник разносторонний')
    else:
        print('это не треугольник')


# 2 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = 1
while (number < 2) | (number > 100000):
    number = int(input('input number from 2 to 100 000 '))
    sostavnoe = 0
    if (number > 2) | (number < 100000):
        for i in range(2, number):
            if (number % i == 0):
                print('число составное')
                exit('')
        print('число простое')


# 3 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(10):
    user_try = int(input('введите число'))
    if (user_try < num):
        print('больше')
    elif (user_try > num):
        print('меньше')
    elif (user_try == num):
        print('угадал')
        exit()
print(num)