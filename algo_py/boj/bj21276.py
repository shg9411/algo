import sys
input = sys.stdin.readline

n = int(input())
names = {}
for name in input().split():
    names[name] = []
m = int(input())
anc = dict()
child = dict()
for _ in range(m):
    x, y = input().split()
    if x not in anc:
        anc[x] = [y]
    else:
        anc[x].append(y)
root = []
for name in names.keys():
    if name in anc:
        for j in anc[name]:
            if j in anc and len(anc[j]) == len(anc[name])-1 or len(anc[name]) == 1:
                if j in child:
                    child[j].append(name)
                else:
                    child[j] = [name]
    else:
        root.append(name)
print(len(root))
print(*sorted(root))
for name in sorted(names.keys()):
    if name in child:
        print(name, len(child[name]), *sorted(child[name]))
    else:
        print(name, 0)
