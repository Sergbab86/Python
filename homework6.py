
i = 0

N = int(input())
while 2 ** i <= N:
    i += 1
d = i - 1
print(d, 2 ** d)
