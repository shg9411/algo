import heapq
import datetime
import time


def comparetime(a, b):
    b = '2021 '+b
    btime = time.mktime(datetime.datetime.strptime(
        b[:-3], '%Y %m/%d %H:%M:%S').timetuple())
    return max(a, btime)+int(b[-2:])*60


def solution(n, customers):
    num = [[] for _ in range(n+1)]
    q = list(zip([0]*n, range(1, n+1)))
    for c in customers:
        k = heapq.heappop(q)
        num[k[1]].append(c)
        t = (comparetime(k[0], c), k[1])
        heapq.heappush(q, t)
    print(num[1:])
    return max(len(arr) for arr in num[1:])


n = 3
customer = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

print(solution(n, customer))
