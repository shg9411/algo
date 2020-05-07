import sys
input = sys.stdin.readline
MAX_NUM = 10000
N = int(input())
A = [int(input()) for _ in range(N)]
count = [0]*(MAX_NUM+1)
#print(sys.getsizeof(count))
countSum = [0]*(MAX_NUM+1)
for i in range(0, N):
    count[A[i]] += 1
countSum[0] = count[0]
for i in range(1, MAX_NUM+1):
    countSum[i] = countSum[i-1]+count[i]
B = [0]*(N+1)
for i in range(N-1, -1, -1):
    B[countSum[A[i]]] = A[i]
    countSum[A[i]] -= 1

for i in range(1, N+1):
    print(B[i])
