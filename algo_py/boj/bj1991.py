n = int(input())

node = [[-1, -1] for _ in range(26)]
for _ in range(n):
    x, y, z = input().split()
    if y.isupper():
        node[ord(x)-65][0] = ord(y)-65
    if z.isupper():
        node[ord(x)-65][1] = ord(z)-65


def preorder(r):
    print(chr(r+65), end='')
    if node[r][0] != -1:
        preorder(node[r][0])
    if node[r][1] != -1:
        preorder(node[r][1])


def inorder(r):
    if node[r][0] != -1:
        inorder(node[r][0])
    print(chr(r+65), end='')
    if node[r][1] != -1:
        inorder(node[r][1])


def postorder(r):
    if node[r][0] != -1:
        postorder(node[r][0])
    if node[r][1] != -1:
        postorder(node[r][1])
    print(chr(r+65), end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)
