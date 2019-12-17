import sys
n = int(sys.stdin.readline())
text = []
for _ in range(n):
    text.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(n):
        if text[i] == text[j][::-1]:
            print(len(text[i]), text[i][len(text[i])//2])
            sys.exit()
