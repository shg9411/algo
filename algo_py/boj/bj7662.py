import bisect
import sys
from collections import deque

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        k = int(input())
        pq = deque()
        pqDict = dict()
        for _ in range(k):
            cmd = input().split()
            val = int(cmd[1])
            if cmd[0] == 'I':
                try:
                    pqDict[val] += 1
                except:
                    pqDict[val] = 1
                    bisect.insort_left(pq, val)
            else:
                if not pq:
                    continue
                if val == -1:
                    if pqDict[pq[0]] == 1:
                        pqDict.pop(pq[0])
                        pq.popleft()
                    else:                    
                        pqDict[pq[0]] -= 1
                else:
                    if pqDict[pq[-1]] == 1: 
                        pqDict.pop(pq[-1])
                        pq.pop()
                    else:
                        pqDict[pq[-1]] -= 1
        if not pq:
            print("EMPTY")
        else:
            print(pq[-1], pq[0])

if __name__=="__main__":
    solve()