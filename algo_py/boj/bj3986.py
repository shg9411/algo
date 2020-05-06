import sys
n = int(sys.stdin.readline())
count = 0
for i in range(n):
    text = sys.stdin.readline().strip()
    stack = []
    for w in text:
        if not stack:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        count += 1
print(count)