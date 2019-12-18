from itertools import combinations
import sys
n, k = map(int, sys.stdin.readline().split())

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
    word = set(sys.stdin.readline().strip()[4:-4])-alpha
    if len(word) <= k-5:
        text.append(word)
        check = check | word
tmp = 0

for c in combinations(check, min(k-5, len(check))):
    count = 0
    for word in text:
        if len(word-set(c)) == 0:
            count += 1
    if tmp < count:
        tmp = count
print(tmp)
