N = int(input())
tree = {}

for i in range(N):
    x, y, z = map(str, input().split())
    if x not in tree:
        tree[x] = dict()
    if y != '.':
        tree[x]['left'] = y
    if z != '.':
        tree[x]['right'] = z

def preorder(r):
    print(r,end='')
    if 'left' in tree[r]:
        preorder(tree[r]['left'])
    if 'right' in tree[r]:
        preorder(tree[r]['right'])
def inorder(r):
    if 'left' in tree[r]:
        inorder(tree[r]['left'])
    print(r,end='')
    if 'right' in tree[r]:
        inorder(tree[r]['right'])

def postorder(r):
    if 'left' in tree[r]:
        postorder(tree[r]['left'])
    if 'right' in tree[r]:
        postorder(tree[r]['right'])
    print(r,end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')