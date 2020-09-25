from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def solve():
    minq = []
    maxq = []
    pd = dict()
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'I':
            if (v := int(cmd[1])) in pd:
                pd[v] += 1
            else:
                pd[v] = 1
                if v >= 0:
                    heappush(maxq, -v)
                else:
                    heappush(minq, v)
        else:
            if not minq and not maxq:
                continue
            if cmd[1] == '1':
                if maxq:
                    if pd[(v := -maxq[0])] > 1:
                        pd[v] -= 1
                    else:
                        heappop(maxq)
                        pd.pop(v)
                else:
                    minq.sort()
                    v = minq[-1]
                    if pd[v] > 1:
                        pd[v] -= 1
                    else:
                        pd.pop(v)
                        minq.pop()
            else:
                if minq:
                    if pd[(v := minq[0])] > 1:
                        pd[v] -= 1
                    else:
                        heappop(minq)
                        pd.pop(v)
                else:
                    maxq.sort()
                    v = -maxq[-1]
                    if pd[v] > 1:
                        pd[v] -= 1
                    else:
                        pd.pop(v)
                        maxq.pop()
    if minq and maxq:
        print(-maxq[0], minq[0])
    elif minq:
        minq.sort()
        print(minq[-1], minq[0])
    elif maxq:
        maxq.sort()
        print(-maxq[0], -maxq[-1])
    else:
        print("EMPTY")


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
