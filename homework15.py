
a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = input('Введите операцию ')


def arithmetic(a, b, c):
    return a, b, c


d = (a, b, c)
if d[2] == '+':
    print(a+b)
elif d[2] == '-':
    print(a-b)
elif d[2] == '*':
    print(a*b)
elif d[2] == '/':
    print(a/b)
else:
    print('Неизвестная операция')
