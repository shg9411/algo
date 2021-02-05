def solve(l, r):
    res = 0
    i = l
    while i < r:
        if s[i] == '(':
            c = int(s[i-1])
            res += c*solve(i+1, v[i])-2
            i = v[i]
            continue
        res += 1
        i += 1
    return res


s = input()
stack = []
v = [0]*50
for i, char in enumerate(s):
    if char == '(':
        stack.append(i)
    elif char == ')':
        v[stack.pop()] = i
print(solve(0, len(s)) if any(v) else len(s))
