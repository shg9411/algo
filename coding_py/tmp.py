import itertools
num = [i for i in range(20)]
for tmp in itertools.combinations(num,10):
    print(tmp)
