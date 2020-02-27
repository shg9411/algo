import sys
input = sys.stdin.readline
n = int(input())
words = input()
tmp = []
hiddennum = ''
for i in range(n):

    if '0' <= words[i] <= '9':
        hiddennum += words[i]
    else:
        tmp.append(hiddennum)
        hiddennum = ''
if hiddennum != '':
    tmp.append(hiddennum)
print(sum(map(int, tmp)) if tmp else 0)
