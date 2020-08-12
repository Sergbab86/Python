
i = 0

N = int(input())
while 2 ** i <= N:
    i += 1
b = i - 1
print(b, 2 ** b)
