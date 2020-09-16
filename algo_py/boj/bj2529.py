import itertools

k = int(input())
sign = input().split()
num = [i for i in range(9, -1, -1)]
selected = []


def dfs(idx, count):
    global find
    if count == k+1 and not find:
        print(''.join(map(str,selected)))
        find = True
        return
    if not find:
        signal = sign[count-1]
        if signal == '>':
            for i in range(idx+1, 10):
                if num[i] not in selected:
                    selected.append(num[i])
                    dfs(i, count+1)
                    selected.pop()
        else:
            for i in range(idx-1, -1, -1):
                if num[i] not in selected:
                    selected.append(num[i])
                    dfs(i, count+1)
                    selected.pop()


find = False
for i in range(10):
    selected.append(num[i])
    dfs(i, 1)
    selected.pop()

selected = []
find = False
for i in range(9, -1, -1):
    selected.append(num[i])
    dfs(i, 1)
    selected.pop()
