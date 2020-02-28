score = []
final = []

for _ in range(8):
    score.append(int(input()))

min_pos = 0

for i in range(8):
    if len(final) < 5:
        final.append(i)
        final.sort()
        if score[i] < score[min_pos]:
            min_pos = i
    else:
        if score[min_pos] < score[i]:
            del final[min_pos]
            final.append(i)
            final.sort()
            min_pos = final[0]
            for i in range(5):
                if final[i] < final[min_pos]:
                    min_pos = i

total = 0
for i in range(5):
    total += score[final[i]]
    final[i] += 1

print(total)
print(" ".join(list(map(str, final))))
