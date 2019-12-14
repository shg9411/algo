import sys
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]
piano = list(map(int, sys.stdin.readline().split()))
if piano == asc:
    print('ascending')
elif piano == des:
    print('descending')
else:
    print('mixed')
