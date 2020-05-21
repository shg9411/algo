n, m = map(int, input().split())
x = [str(i) for i in sorted(map(int, input().split()))]
x_ = [' '+i for i in x]
print(x_)
#print(x_)
for _ in range(m-1):
    x = [i + j for i in x for j in x_]
# print('\n'.join(x))
