import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    pkmn = []
    pkmn_dic = {}
    res = []
    for i in range(1,n+1) :    
        pk = input().rstrip()
        pkmn.append(pk)
        pkmn_dic[pk] = i
    for _ in range(m):
        query = input().rstrip()
        if query.isdigit() :
            res.append(pkmn[int(query)-1])
        else :
            res.append(str(pkmn_dic[query]))
    print('\n'.join(res))
        
if __name__=='__main__':
    solve()