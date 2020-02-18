import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                #print(data,self.data,'오른쪽 노드에 삽입')
                self.right = Node(data)
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                #print(data,self.data,'왼쪽 노드에 삽입')
                self.left = Node(data)

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)


root = Node(int(input()))


while 1:
    try:
        root.insert(int(input()))
    except:
        break

root.postorder()
