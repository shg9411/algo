import sys
n = int(input())

class Queue(list):
    push = list.append
    def pop(self):
        list.pop(0)

q = Queue()

for _ in range(n):
    tmp = sys.stdin.readline().split()
    
    q.push(3)
    q.pop()
    print(q)