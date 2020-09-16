from itertools import permutations


def calc(arr):
    res = 0
    for i in range(len(arr)-1):
        res += abs(arr[i]-arr[i+1])
    print(arr,res)
    return res

tmp = -1000
n = int(input())
for x in permutations(map(int, input().split())):
    tmp = max(tmp,calc(x))

print(tmp)
