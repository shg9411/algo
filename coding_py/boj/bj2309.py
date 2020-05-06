import itertools
key = []
for _ in range(9):
    key.append(int(input()))

tmp = list(itertools.combinations(key, 7))

for t in tmp:
    if sum(t) == 100:
        print('\n'.join(map(str, sorted(t))))
        break
