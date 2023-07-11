import datetime
import logging
from sys import argv
from random import randint

# 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# для запуска из терминала -  python .\main.py 5 51 56

logging.basicConfig(filename='error.log', level=logging.NOTSET, encoding='UTF-8')

if __name__ == '__main__':

    logging.info(f'start at {datetime.datetime.now()}')
    try:
        _, side_a, side_b, side_c = argv
        print(side_a,side_b,side_c)
    except ValueError as e0:
        logging.error(f'введено неверное количество параметров')
        logging.info(f'end at {datetime.datetime.now()}')
    except NameError as e00:
        pass

    def check_triangle(side_a, side_b, side_c):

        try:
            if (side_a + side_b > side_c) & (side_b + side_c > side_a) & (side_a + side_c > side_b):
                if (side_a == side_b == side_c):
                    print('треугольник равносторонний')
                    logging.info('треугольник равносторонний')
                elif (side_a == side_b) | (side_b == side_c) | (side_a == side_c):
                    print('треугольник равнобедренный')
                    logging.info('равнобедренный')
                elif (side_a != side_b != side_c):
                    print('треугольник разносторонний')
                    logging.info('разносторонний')
            else:
                if (side_a == 0) | (side_b == 0) | (side_c == 0):
                    print('это не треугольник, одна из сторон = 0')
                    logging.warning(f'это не треугольник, одна из сторон = 0')
                else:
                    print('это не треугольник')
                    logging.warning(f'это не треугольник')
        except TypeError as e1:
            logging.error(f'Ошибка типа даных {e1}')

        except NameError as e2:
            logging.error(f'Ошибка переменная не определена {e2}')

        logging.info(f'end at {datetime.datetime.now()}')


    check_triangle(side_a,side_b,side_c)







# # 2 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# # Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# # Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
#
# number = 1
# while (number < 2) | (number > 100000):
#     number = int(input('input number from 2 to 100 000 '))
#     sostavnoe = 0
#     if (number > 2) | (number < 100000):
#         for i in range(2, number):
#             if (number % i == 0):
#                 print('число составное')
#                 exit('')
#         print('число простое')
#
#
# # 3 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# # Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# # Для генерации случайного числа используйте код:
# # from random import randint
# # num = randint(LOWER_LIMIT, UPPER_LIMIT)
#
# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
# for i in range(10):
#     user_try = int(input('введите число'))
#     if (user_try < num):
#         print('больше')
#     elif (user_try > num):
#         print('меньше')
#     elif (user_try == num):
#         print('угадал')
#         exit()
# print(num)