
a = int(input('Год: '))


def is_year_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year // 100 != 0):
        print('True')
    else:
        print('False')


is_year_leap(a)