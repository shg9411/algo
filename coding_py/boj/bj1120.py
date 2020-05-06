a,b = input().split()
min = len(b)
count = 0
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    print(count)
else:
    for i in range(len(b)-len(a)+1):
        for j in range(len(a)):
            if a[j] != b[i+j]:
                count+=1
        if min > count:
            min = count
        count = 0
    print(min)