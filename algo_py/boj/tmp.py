n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
num = 0
for n in a:
    tmp = 987654321
    for m in b:
        tmp = min(tmp, (n & m) | num)
    num = tmp
print(num)
