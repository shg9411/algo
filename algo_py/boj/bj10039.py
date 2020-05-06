score = 0
for _ in range(5):
    tmp = int(input())
    if tmp < 40:
        score += 40
    else:
        score += tmp
print(score//5)
