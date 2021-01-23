N = int(input())
ls = sorted((map(int,input().split())))
M = int(input())
ls2 = list(map(int,input().split()))

def bin_search(a,key):
    bl = 0
    br = len(a) - 1
    while True:
        bc = (bl+br)//2
        if a[bc] == key:
            print(1)
            break
        elif bc > key:
            br = bc - 1
        else:
            bl = bc + 1
        if bl>br:
            print(0)
            break

for i in ls2:
    bin_search(ls,i)