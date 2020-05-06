import sys
import operator
input = sys.stdin.readline
n = int(input())
stu = []
for _ in range(n):
    tmp = input().split()
    stu.append([tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])])
stu = sorted(sorted(sorted(sorted(stu, key=operator.itemgetter(0)), key=operator.itemgetter(
    3), reverse=True), key=operator.itemgetter(2)), key=operator.itemgetter(1), reverse=True)

for s in stu:
    print(s[0])