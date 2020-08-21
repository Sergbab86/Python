
import random

lst = []
for _ in range(10):
    lst.append(random.randint(10, 100))
print(lst)
k = int(input('Введите ндекс >=0 и <={}: ' .format(len(lst) - 1)))
c = int(input('Введите число:'))

lst.append(0)
for idx in range(len(lst)-1, k, -1):
    lst[idx] = lst[idx-1]
lst[k] = c
print(lst)
