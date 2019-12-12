n, m = map(int, input().split())

dna = [list(input()) for _ in range(n)]
hd = ['A', 'C', 'G', 'T']
result = []
count = 0
for i in range(m):
    acgt = [0]*4
    for j in range(n):
        count += 1
        if dna[j][i] == 'A':
            acgt[0] += 1
        elif dna[j][i] == 'C':
            acgt[1] += 1
        elif dna[j][i] == 'G':
            acgt[2] += 1
        else:
            acgt[3] += 1
    result.append(hd[acgt.index(max(acgt))])
    count -= max(acgt)

print(''.join(result))
print(count)
