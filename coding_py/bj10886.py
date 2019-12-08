n = int(input())
i = []
for _ in range(n):
    i.append(int(input()))
if sum(i)/n > 0.5:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
