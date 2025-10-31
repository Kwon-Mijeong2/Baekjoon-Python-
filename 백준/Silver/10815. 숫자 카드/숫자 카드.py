import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))
    
dictionary = {}
for i in range(n):
    dictionary[lst[i]] = -1

# 출력
for i in lst2:
    if i in dictionary:
        print(1, end=" ")
    else:
        print(0, end=" ")