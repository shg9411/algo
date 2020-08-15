card = dict()
for tmp in map(int, __import__('sys').stdin.read().split()[1:]):
    if tmp not in card:card[tmp] = 1
    else:card[tmp] += 1
print(sorted(card.items(), key=lambda a: (-a[1], a[0]))[0][0])