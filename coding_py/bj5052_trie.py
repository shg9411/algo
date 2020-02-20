import sys
input = sys.stdin.readline
t = int(input())


class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.flag = False


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, text):
        current = self.head
        for char in text:
            if char not in current.children:
                current.children[char] = Node(char)
            else:
                if current.children[char].flag:
                    return True

            current = current.children[char]
        current.flag = True


for _ in range(t):
    trie = Trie()
    n = int(input())
    tmp = []
    res = False
    for _ in range(n):
        tmp.append(input().rstrip())
    tmp.sort()
    for text in tmp:
        if trie.insert(text):
            res = True
            break
    print("NO" if res else "YES")
