N, M = map(int, input().split())
cards = list(reversed(sorted(map(int, input().split()))))
sumSet = set()
blackjack = False
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum == M:
                blackjack = True
                break
            elif sum < M:
                sumSet.add(sum)
                break
        if blackjack:
            break
    if blackjack:
        break
if blackjack:
    print(M)
else:
    print(max(sumSet))