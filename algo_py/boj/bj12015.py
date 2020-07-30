import bisect
input()
lis = []
for num in map(int, input().split()):
    if not lis:
        lis.append(num)
        continue
    if lis[-1]<num:
        lis.append(num)
    else:
        lis[bisect.bisect_left(lis,num)] = num
print(len(lis))
