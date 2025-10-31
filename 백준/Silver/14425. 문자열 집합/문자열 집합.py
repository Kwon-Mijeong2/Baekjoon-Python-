import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

s = {}
cnt = 0

for _ in range(n):
    s[input().rstrip()] = 0

for _ in range(m):
    if input().rstrip() in s:
        cnt += 1

print(cnt)