import sys
import operator
input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    tmp = input().split()
    people.append((int(tmp[0]), tmp[1], i))
people.sort(key=operator.itemgetter(0, 2))
for person in people:
    print(person[0], person[1])
