import sys


def check(i):
    tmp = set(str(i))
    if i % 3 == 0 or '3' in tmp or '6' in tmp or '9' in tmp:
        return True


a, b = map(int, sys.stdin.readline().split())
count = 0
for i in range(a, b+1):
    if check(i):
        count += 1

print(count % 20150523)
