import sys
n = int(input())
dic = list(set([sys.stdin.readline().strip() for _ in range(n)]))
dic = sorted(dic, key=lambda x: (len(x), x))
print('\n'.join(dic))