text = "HELLO"

# print(text[::-1])

# for문 사용


def printReverse(text):
    length = len(text)
    for i in range(length):
        print(text[length-i-1], end='')


printReverse(text)
