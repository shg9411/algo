import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx, val):
    if idx == len(tmp):
        print(''.join(val))
        return
    for i in range(26):
        if arr[i]:
            arr[i] -= 1
            val.append(chr(i+ord('a')))
            dfs(idx+1, val)
            val.pop()
            arr[i] += 1


n = int(input())
for _ in range(n):
    tmp = input().rstrip()
    arr = [0 for _ in range(26)]
    for char in tmp:
        arr[ord(char)-ord('a')] += 1
    dfs(0, [])
