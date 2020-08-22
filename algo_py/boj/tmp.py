import sys
input = sys.stdin.readline
cur = (1 << 26)-1
n, m = map(int, input().split())
word = [0 for _ in range(n)]
for i in range(n):
    w = input().rstrip()
    for char in w:
        idx = ord(char)-97
        word[i] |= 1 << idx

for _ in range(m):
    query = input().split()
    cnt = 0
    idx = ord(query[1])-97
    if query[0] == '1':
        cur &= ~(1 << idx)
    else:
        cur |= 1 << idx
    for w in word:
        if (cur & w) == w:
            cnt += 1
    print(cnt)
