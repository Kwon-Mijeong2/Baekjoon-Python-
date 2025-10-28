import sys

n = int(sys.stdin.readline())
lst = [0] * 100001

for i in range(n):
    a = int(sys.stdin.readline())
    lst[a] += 1

for i in range(1, 10001):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)