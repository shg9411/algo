import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    num, word = input().split()
    num = int(num)
    print(word[:num-1]+word[num:])
