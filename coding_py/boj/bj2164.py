from collections import deque
n = int(input())

card = deque([i for i in range(1, n+1)])

while 1:
    if len(card) == 1:
        print(card.popleft())
        break
    card.popleft()
    card.rotate(-1)
