import sys
input = sys.stdin.readline

t = int(input())

tri = [0, 1]

i = 1

while 1:
    i += 1
    tmp = tri[i-1] + i
    if tmp > 1000:
        break
    tri.append(tmp)

triLen = len(tri)

for _ in range(t):
    k = int(input())
    finish = False
    for i in range(1, triLen):
        if finish:
            break
        if tri[i] >= k:
            break
        for j in range(1, triLen):
            if finish:
                break
            tmp = tri[i] + tri[j]
            if tmp >= k:
                break
            for l in range(1, triLen):
                if tmp + tri[l] == k:
                    print(1)
                    finish = True
                    break
                if tmp + tri[l] > k:
                    break
    if not finish:
        print(0)
