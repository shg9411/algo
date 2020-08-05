import sys
input = sys.stdin.readline

n = int(input())

node = [[] for _ in range(n+1)]

info = list(map(int, input().split()))
for idx, parent in enumerate(info):
    node[parent+1].append(idx)


def cutChildren(n):
    if node[n+1] == []:
        node[n+1]=[-1]
        return
    for c in node[n+1]:
        cutChildren(c)
    node[n+1] = [-1]

#print(node)
cut = int(input())
if cut==node[0]:
    print(0)
    exit()

for n in node:
    if cut in n:
        n.remove(cut)

cutChildren(cut)
#print(node)
count = 0
for n in node[1:]:
    if n==[]:
        count+=1
print(count)
