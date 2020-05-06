import sys
input = sys.stdin.readline

before = input().rstrip()
after = input().rstrip()
bl = len(before)
al = len(after)
length = min(bl, al)
idx = -1
for i in range(length):
    idx = i
    if before[i] != after[i]:
        break

length -= idx
diff = length
for i in range(length):
    if before[bl-i-1] != after[al-i-1]:
        diff = i
        break

print(al - diff - idx)
