
s = int(input('Сторона квадрата: '))


def square(s):
    x = s * 4
    y = s ** 2
    z = (2 ** 0.5)*s
    return x, y, z


square(s)
x1, y1, z1 = square(s)
print(x1, y1, z1)
