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
