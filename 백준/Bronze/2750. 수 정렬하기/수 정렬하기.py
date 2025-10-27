a = int(input())
lst = []

for i in range(a):
    lst.append(int(input()))
lst2 = sorted(lst)

for i in range(len(lst)):
    print(lst2[i])