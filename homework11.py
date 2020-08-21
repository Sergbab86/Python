
h = 13
if h % 2 == 0:
    h += 1
for i in range(h // 2 + 1):
    for j in range(h):
        if (
                i == h // 2
                or j == h // 2 + i
                or i == h // 2 - j
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

for i in range(h // 2 + 1):
    for j in range(h):
        if (
                i == h // 2
                or (j <= h //2 + i and i >= h // 2 - j)
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()


for i in range(h):
    for j in range(h):
        if (
                i == h // 2
                or (j <= h //2 + i and i >= h // 2 - j and i < h // 2)
                or (j == i - h // 2 and i > h // 2)
                or (j == h - i + (h // 2 - 1) and i > h // 2)
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

for i in range(h):
    for j in range(h):
        if (
                i == h // 2
                or (j <= h //2 + i and i >= h // 2 - j and i < h // 2)
                or (j == i - h // 2 and i > h // 2)
                or (j == h - i + (h // 2 - 1) and i > h // 2)
                or j == h // 2
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()
