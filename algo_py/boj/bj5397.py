import sys
input = sys.stdin.readline


def solve():
    front = []
    back = []
    for char in input().rstrip():
        if char in '<>-':
            if char == '<':
                if front:
                    back.append(front.pop())
            elif char == '>':
                if back:
                    front.append(back.pop())
            else:
                if front:
                    front.pop()
        else:
            front.append(char)
    print(''.join(front), ''.join(back[::-1]), sep='')


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()