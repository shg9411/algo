import sys
input = sys.stdin.readline
class CList:
    class Node:
        def __init__(self,item,link):
            self.item = item
            self.next = link
    
    def __init__(self):
        self.last = None
        self.size = 0
    
    def insert(self,item):
        n = self.Node(item,None)
        if(self.size == 0):
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1
    
    def delete(self,p):
        x = p.next
        if(self.size == 1):
            self.last = None
        else:
            p.next = x.next
        self.size -= 1
        return x.item

    def print_list(self,N,K):
        s = ''
        p = self.last
        for _ in range(N):
            for j in range(K-1):
                p = p.next
            s += str(self.delete(p))
        return s

N,K = map(int,input().split())
c = CList()
for i in range(N,0,-1):
    c.insert(i)
print("<",end='')
print(', '.join(c.print_list(N,K)),end='')
print(">")