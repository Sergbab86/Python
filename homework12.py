
import random

k = 5
lst = []
for _ in range(20):
    lst.append(random.randint(10, 50))
lst.pop(k)
print(lst)
