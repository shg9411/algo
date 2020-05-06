import sys
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
    sys.exit()
print(a//(c-b)+1)
