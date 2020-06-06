import sys
from collections import defaultdict
from operator import itemgetter
input = sys.stdin.readline

N = int(input())
league = defaultdict(lambda: [0, 0])
for _ in range(N*(N-1)):
    a, awin, b, bwin = input().split()
    res = int(awin) - int(bwin)
    if res > 0:
        league[a][0] += 1
    else:
        league[b][0] += 1
    league[a][1] += res
    league[b][1] -= res

for val in sorted(sorted(league.items()), key=lambda i: i[1], reverse=True):
    print("{} {} {}".format(val[0], val[1][0], val[1][1]))
