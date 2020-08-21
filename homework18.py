
m = int(input('Месяц номер: '))


def season(month):
    if m >=1 and m<=3:
        print('Зима')
    elif m >= 4 and m <= 5:
        print('Весна')
    elif m >= 6 and m <=8:
        print('Лето')
    else:
        print('Зима')


season(m)
