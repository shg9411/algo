import sys
cnt = 0
for line in sys.stdin:
    cnt+=line.count('joke')
print(cnt)