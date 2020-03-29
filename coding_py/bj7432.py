import sys
input = sys.stdin.readline

n = int(input())


class directory:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, arr):
        if not self.children:
            self.children = [directory(arr[0])]
        else:
            if not self.findChild(arr[0]):
                self.children.append(directory(arr[0]))
        if arr[1:]:
            self.findChild(arr[0]).addChild(arr[1:])

    def findChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return False

    def __gt__(self, another):
        return self.name > another.name


root = directory('root')

for _ in range(n):
    tmp = input().rstrip().split('\\')
    root.addChild(tmp)


def printChild(root, indent):
    root.children.sort()
    for child in root.children:
        print(indent*' ', end='')
        print(child.name)
        printChild(child, indent+1)


printChild(root, 0)
