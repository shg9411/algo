import itertools
import sys
sys.setrecursionlimit(10**6)


def postorder(preorder):
    if not preorder:
        return []
    else:
        root = preorder[0]
        left = list(itertools.takewhile(lambda x: x < root, preorder[1:]))
        right = preorder[len(left) + 1:]
        return postorder(left) + postorder(right) + [root]


if __name__ == '__main__':
    preorder = []
    while 1:
        try:
            preorder.append(int(input()))
        except:
            break
    print('\n'.join(str(x) for x in postorder(preorder)))
