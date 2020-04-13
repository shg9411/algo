import itertools

num = [i for i in range(1, 4)]
ans = 0
for tmp in list(itertools.product(num, repeat=2)):
    if sum(tmp) == 4:
        ans += 1

print(ans)
