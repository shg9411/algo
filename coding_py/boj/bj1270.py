import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    t = list(map(int, input().split()))
    tmp = dict()
    for num in t[1:]:
        try:
            tmp[num] += 1
        except:
            tmp[num] = 1
    number = sorted(tmp.items(), key=lambda x: x[1])
    if number[-1][1] > t[0]/2:
        print(number[-1][0])
    else:
        print("SYJKGW")

l = []
for x in range(0, 50):
    for y in range(0, 50):
        if hash((x, y)) in l:
            print("Fail: ", (x, y))
        l.append(hash((x, y)))
print("Test Finished")
