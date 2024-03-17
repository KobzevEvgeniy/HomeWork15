# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
import argparse

import days_parsing
from days_parsing import TextToDate

if __name__ == '__main__':
    arg_pars = argparse.ArgumentParser(description='Определение даты из строки')
    arg_pars.add_argument('texts', metavar='S', type=str, nargs='*', help='дата в виде: "1-й четверг ноября"')
    args = arg_pars.parse_args()

    test = TextToDate()
    if len(args.texts) > 0:
        print('Run set of user\'s tests')
        for text in args.texts:
            print(test(text))
    else:
        print('Run set of tests default')
        print(test('1-й четверг ноября'))  # 2023-11-02
        print(test('3-я среда мая'))  # 2023-05-17
        print(test.date)  # без лога, обращение к параметру
        print(test('5-я среда мая'))  # WeekNumberError
        print(test('2-я середина мая'))  # WeekDayNameError
        print(test('2-я среда месяца'))  # MonthNameError
        print(test())  # Wrong Argument
        print(test(''))  # Wrong Argument

    def out_parser():
        parser = argparse.ArgumentParser(description="My first argument parser from terminal")
        parser.add_argument('--name', metavar='N', type=float,
                            nargs='*', help='press some numbers')
        args = parser.parse_args()
        print(f'В скрипт передано: {args}')

        return parser.parse_args()
    out = out_parser()
    test(out)
    print(out)

