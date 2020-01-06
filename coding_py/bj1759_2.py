import sys
input = sys.stdin.readline

l, c = map(int, input().split())

char = sorted(list(input().split()))
select = [False] * c
vowels = ('a', 'e', 'i', 'o', 'u')


def check(word):
    num = 0
    for char in word:
        if char in vowels:
            num += 1
    if num >= 1 and len(word)-num >= 2:
        print(word)


def makeWord(word, idx, count):
    if count == l:
        check(word)
        return
    for i in range(idx, c):
        # if select[i]:
        #    continue
        select[i] = True
        makeWord(word+char[i], i+1, count+1)
        select[i] = False


makeWord('', 0, 0)
