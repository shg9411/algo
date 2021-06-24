import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
dictObj = {}
for _ in range(n):
    word = input().rstrip()
    length = len(word)
    if length < m:
        continue
    dictObj[word] = dictObj.get(word, 0)+1

for k, _ in sorted(dictObj.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(k)