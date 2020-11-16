import sys
input = sys.stdin.readline

board = dict()
for _ in range(int(input())):
    name, score = input().split()
    board[name] = int(score)

print(sorted(board.items(), key=lambda x: (-x[1], x[0]))[0][0])
