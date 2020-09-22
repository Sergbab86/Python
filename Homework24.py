
from random import randint

rows = 8
cols = 10

lst = [[randint(10, 80) for _ in range(cols)] for _ in range(rows)]
print(lst)

print(lst[0])
print(lst[0][1])

s = 0
lst1 = []

for i in range(len(lst)):
    for j in range(len(lst[i])):
        s += lst[i][j]
        print('{:>3}'.format(lst[i][j]), end=' ')
    print(' ', s)
    s = 0


print(lst1)


