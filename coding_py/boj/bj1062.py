from itertools import combinations
import sys
input = input
n, k = map(int, input().split())

if k < 5:
    print(0)
    sys.exit()
if k == 26:
    print(n)
    sys.exit()
text = []
alpha = set('acint')
check = set()

for _ in range(n):
    word = set(input().strip()[4:-4])
    text.append(word)
    check |= word
check -= alpha
tmp = 0

for c in combinations(check, min(k-5, len(check))):
    count = 0
    subset = set(c) | alpha
    for word in text:
        if word <= subset:
            count += 1
    if tmp < count:
        tmp = count
print(tmp)
