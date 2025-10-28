lst =[]
m = 0

for i in range(5):
    lst.append(int(input()))
    m += lst[i]
lst2 = sorted(lst)

print(int(m / 5))
print(lst2[2])