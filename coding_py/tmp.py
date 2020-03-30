input = __import__('sys').stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
L = [*range(-1, n - 1), -1]
R = [*range(1, n + 1), n]
d = [0] * (n + 1)

for t in reversed(a):
	l = L[t]
	r = R[t]
	d[t] = (l, r)
	L[r] = l
	R[l] = r
for t in a:
	l, r = d[t]
	d[t] = max(d[l], d[r]) + 1
print(sum(d))