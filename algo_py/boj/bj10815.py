import sys
if __name__=='__main__':
    input()
    x = set(input().split())
    input()
    sys.stdout.write(' '.join(['1' if i in x else '0' for i in input().split()]))