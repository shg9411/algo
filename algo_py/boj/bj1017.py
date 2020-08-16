import sys
input = sys.stdin.readline


# 범위 내의 소수 구해놓기
N = 2001
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False


# 이분매칭
def dfs(i):
    for num in candi[i]:
        if not check[num]:
            check[num] = True
            if bmatch[num] == -1 or dfs(bmatch[num]):
                amatch[i] = num
                bmatch[num] = i
                return True
    return False


n = int(input())
a = []
b = []
cnt = n//2
# 숫자마다 더했을 때 소수가 되는 쌍 구해놓을 후보 리스트
candi = [[] for _ in range(cnt)]
ans = []
tmp = -1

# a에 짝수 b에 홀수 저장
for num in map(int, input().split()):
    if tmp == -1:
        tmp = num
    if num & 1:
        b.append(num)
    else:
        a.append(num)

# 짝+짝이나 홀+홀은 소수가 될 수 없음
# 짝과 홀의 개수가 같아야 확인해 볼 가치가 있음
if len(a) != len(b):
    print(-1)
    exit()

# 첫번째 수가 홀수이면 a,b교환
if tmp % 2 == 1:
    a, b = b, a

# 후보들 저장
for i, f in enumerate(a):
    for j, s in enumerate(b):
        if sieve[f+s]:
            candi[i].append(j)

# 첫번째 수 후보들에 대해서 이분매칭
for num in candi[0]:
    amatch = [-1 for _ in range(cnt)]
    bmatch = [-1 for _ in range(cnt)]
    # 첫번째 수의 후보는 처리해놓고
    # 나머지 수들에 대해서 탐색
    matching = 1
    amatch[0] = num
    bmatch[num] = 0
    for i in range(1, cnt):
        check = [False for _ in range(cnt)]
        check[num] = True
        if dfs(i):
            matching += 1
    # 모든 쌍이 매칭되었다면 ans에 추가
    if matching == cnt:
        ans.append(b[num])

if not ans:
    print(-1)
else:
    print(*sorted(ans))
