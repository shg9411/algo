import sys

N = int(sys.stdin.readline())
count = 0
lst = []
room = [0]*100000

for i in range(N):
    case = list(map(int, sys.stdin.readline().split()))
    case.append(case[1]-case[0])
    lst.append(case)

lst = sorted(lst, key=lambda x: (x[2], -x[1]))

for i in lst:

    if room[int(i[0]):int(i[1])] == [0]*int(i[2]) and int(i[2] != 0):
        room[int(i[0]):int(i[1])] = [1] * (int(i[2]))
        count += 1

    if int(i[2]) == 0:
        count += 1

print(count)