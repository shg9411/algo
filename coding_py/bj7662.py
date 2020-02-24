import bisect  # 이진 탐색 알고리즘
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    pq = deque()  # deque 생성
    pqDict = dict()  # 같은 값이 존재할 수 있기에 hash로 구현된 dict 생성
    for _ in range(k):
        cmd = input().split()
        val = int(cmd[1])
        if cmd[0] == 'I':  # 삽입 시
            try:
                pqDict[val] += 1  # 이미 deque에 값이 존재하면 dict에서 value값 증가
            except:
                pqDict[val] = 1  # 새로운 값이 들어오면 dict에 삽입
                bisect.insort_left(pq, val)  # 이진탐색으로 위치 파악 후 삽입
        else:
            if not pq:  # deque가 비어있으면 continue
                continue
            if val == -1:  # 최솟값 삭제시
                if pqDict[pq[0]] == 1:  # 최솟값이 deque에 하나만 존재할 때
                    pqDict.pop(pq[0])  # dict에서 값 제거
                    pq.popleft()  # deque에서 값 제거
                else:
                    # 최솟값이 deque에 하나 이상이면 dict에서 value값만 마이너스
                    pqDict[pq[0]] -= 1
            else:
                if pqDict[pq[-1]] == 1:  # 최댓값 삭제시 같은 방법으로 진행
                    pqDict.pop(pq[-1])
                    pq.pop()
                else:
                    pqDict[pq[-1]] -= 1
    if not pq:
        print("EMPTY")
    else:
        print(pq[-1], pq[0])
