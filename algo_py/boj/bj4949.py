import sys
input = sys.stdin.readline


def solve(t):
    tmp = []
    for char in t:
        if char == ')':
            if tmp and tmp[-1] == '(':
                tmp.pop()
            else:
                return False
        elif char == ']':
            if tmp and tmp[-1] == '[':
                tmp.pop()
            else:
                return False
        elif char == '(' or char == '[':
            tmp.append(char)
        else:
            continue
    return True if not tmp else False


if __name__ == '__main__':
    r = []
    while 1:
        t = input()
        if t == ".\n":
            print('\n'.join(r))
            break
        r.append("yes" if solve(t) else "no")
