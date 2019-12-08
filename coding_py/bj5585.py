n = 1000-int(input())
coin = [500, 100, 50, 10, 5, 1]
count = 0
for c in coin:
    if n >= c:
        count += n//c
        n %= c
print(count)
