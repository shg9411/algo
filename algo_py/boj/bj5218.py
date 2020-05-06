import sys
tc = int(input())
for _ in range(tc):
    a, b = sys.stdin.readline().split()
    print('Distances: ', end='')
    for i in range(len(a)):
        result = ord(b[i]) - ord(a[i])
        print(result if result >= 0 else result+26, end=' ')
    print()
