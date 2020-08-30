
from random import randint

lst = [randint(1, 100) for _ in range(20)]
print(lst)
s = '-'.join(map(str, lst))
print(s)


def reverse_func(s):
    lst1 = list(s)
    for i in range(len(s) // 2):
        tmp = lst1[i]
        lst1[i] = lst1[len(s) - i -1]
        lst1[len(s) - i - 1] = tmp
    return ''.join(lst1)


lst = reverse_func(s)
print(lst)