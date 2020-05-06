import sys
T = int(sys.stdin.readline())
results = []

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    R = []
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        R.append([X, Y])
    W = int(sys.stdin.readline())

    operating_map = {}
    for building, time in enumerate(D):
        operating_map[building+1] = time

    rule_map = {}
    for i in range(N):
        rule_map[i+1] = set()
    for rule in R:
        X = rule[0]
        Y = rule[1]
        rule_map[Y].add(X)

    done = set()
    time = 0

    while W not in done:

        bases = []
        for building in rule_map:

            if done.issuperset(rule_map[building]) and building not in done:
                bases.append(building)

        time_step = min([operating_map[base] for base in bases])
        time += time_step

        for base in bases:
            operating_map[base] -= time_step

            if operating_map[base] == 0:
                done.add(base)

    results.append(time)

for result in results:
    sys.stdout.write(str(result)+'\n')
