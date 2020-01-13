import sys
sys.setrecursionlimit(10**6)

def Z(N, r, c, num, x, y):
    if x!=r or y!=c:
        num+=1
        if (x+1)%2==0:
            if (y+1)%2==0 and (y+1)==2**N:
                return Z(N, r, c, num, x+1, 0)
            elif (y+1)%2==0 and (y+1)!=2**N:
                return Z(N, r, c, num, x-1, y+1)
            else: return Z(N, r, c, num, x, y+1)
        else:
            if (y+1)%2==0:
                return Z(N, r, c, num, x+1, y-1)
            else: return Z(N, r, c, num, x, y+1)
    else: return num
    
N, r, c = map(int, input().split())
value = Z(N, r, c, 0, 0, 0)
print(value)