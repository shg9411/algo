k = int(input())-1
count = 0

while k:
    count += k & 1
    k >>= 1
print(count & 1)
