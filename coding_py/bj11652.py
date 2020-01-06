import sys
import operator
input = sys.stdin.readline

n = int(input())

card = dict()

for _ in range(n):
    tmp = int(input())
    if tmp not in card:
        card[tmp] = 1
    else:
        card.update({tmp: card[tmp]+1})

k = sorted(sorted(list(zip(card.keys(), card.values())),key = operator.itemgetter(0)),key = operator.itemgetter(1), reverse=True)
print(k[0][0])
