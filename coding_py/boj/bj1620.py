import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pkmn = []
pkmn_dic = {}

for i in range(n):
    pk = input().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1
print(pkmn)
print(pkmn_dic)
for _ in range(m):

    query = input().rstrip()

    if query.isdigit():
        print(pkmn[int(query)-1])
    else:
        print(pkmn_dic[query])
