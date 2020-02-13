import sys

ans = [0] * 1000001

tc = int(sys.stdin.readline())

for i in range(1,1000001):
    for j in range(i,1000001,i):
        ans[j] += i
    ans[i] += ans[i-1]
for _ in range(tc):
    sys.stdout.write("{}\n".format(ans[int(sys.stdin.readline())]))