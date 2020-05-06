import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

invite = set()

for friend in friends[1]:
    invite.add(friend)
    for f_o_f in friends[friend]:
        invite.add(f_o_f)
print(len(invite)-1)
