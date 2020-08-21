
import random

lst1 = [random.randint(10, 50) for _ in range(5)]
lst2 = [random.randint(10, 50) for _ in range(5)]
print(lst1)
print(lst2)
res = len(set(lst1 + lst2))
print(res)