
i = 0

N = int(input())
while 2 ** i <= N:
    i += 1
print(i - 1, 2 ** (i - 1))
