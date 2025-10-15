n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            t = lst[i] + lst[j] + lst[k]

            if (t > m):
                continue
            else:
                lst2.append(t)

print(max(lst2))