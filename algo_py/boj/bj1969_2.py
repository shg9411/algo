import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hd = [list(input().rstrip()) for _ in range(n)]
hd = list(zip(*hd))
res = ''
count = 0
for line in hd:
    tmp = []
    tmp.append(line.count('A'))
    tmp.append(line.count('C'))
    tmp.append(line.count('G'))
    tmp.append(line.count('T'))
    if 0 == tmp.index(max(tmp)):
        res += 'A'
        count += sum(tmp[1:])
    elif 1 == tmp.index(max(tmp)):
        res += 'C'
        count += sum(tmp[0:1])+sum(tmp[2:4])
    elif 2 == tmp.index(max(tmp)):
        res += 'G'
        count += sum(tmp[0:2])+tmp[3]
    elif 3 == tmp.index(max(tmp)):
        res += 'T'
        count += sum(tmp[:3])
print(res)
print(count)
