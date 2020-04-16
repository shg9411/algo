import sys
S = list(map(int, sys.stdin.readline().rstrip()))
print(S)
S.sort(reverse=True)
print(''.join(str(i) for i in S))
