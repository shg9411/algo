def isOk(num):
    length = len(num)
    s = 1
    e = length//2
    for i in range(s, e+1):
        if num[-1:-(i+1):-1] == num[-(i+1):-i*2-1:-1]:
            return False
    return True


def dfs(n, num):
    if n == N:
        print(num)
        exit()
    for i in '123':
        if isOk(num+i):
            dfs(n+1, num+i)


if __name__ == '__main__':
    N = int(input())
    dfs(1, '1')
