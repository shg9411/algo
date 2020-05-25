import re
import sys
input = sys.stdin.readline


def check():
    p = re.compile('(100+1+|01)+$')
    print("NO" if p.match(input().rstrip()) == None else "YES")


if __name__ == '__main__':
    for _ in range(int(input())):
        check()
