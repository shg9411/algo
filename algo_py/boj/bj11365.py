import sys
input = sys.stdin.readline

while 1:
    string = input().rstrip()
    if string == 'END':
        break
    print(string[::-1])
