def is_valid(s):
    stack = []
    for ch in s:
        if ch in "(":
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (ch == ")" and top != "("):
                return False
    return len(stack) == 0

s = []
n = int(input())
for i in range(n):
    s.append(input())

for i in range(n):
    if is_valid(s[i]) == True:
        print("YES")
    else:
        print("NO")