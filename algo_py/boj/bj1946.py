import sys
input = sys.stdin.readline


for _ in range(int(input())):
    people = []
    count = 0
    for _ in range(int(input())):
        people.append(list(map(int, input().split())))
    people.sort()
    x = y = len(people)+1
    for p in people:
        ok = False
        if p[0] < x:
            x = p[0]
            ok = True
        if p[1] < y:
            y = p[1]
            ok = True
        if ok:
            count += 1
    print(count)
