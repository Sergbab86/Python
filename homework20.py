#
# n = int(input())
#
# b = ''
#
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
#
# lst = list(b)
#
# print(type(b), b)
# print(type(lst), lst)


num = int(input())
base = int(input("Base (2-9): "))
if not(2 <= base <= 9):
    quit()

newNum = ''

while num > 0:
    newNum = str(num % base) + newNum
    num //= base

print(newNum)