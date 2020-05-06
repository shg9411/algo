import sys
input = sys.stdin.readline

n = int(input())

people = []

for i in range(n):
    people.append(list(map(int, input().split())))
res = []
for i in range(n):
    count = 1
    for j in range(n):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                count += 1
    res.append(count)
print(' '.join(map(str, res)))
