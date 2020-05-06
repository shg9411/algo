n = int(input())


def hanoi(a, start, mid, end):
    if a == 1:
        print(start, end)
        return
    hanoi(a-1, start, end, mid)
    print(start, end)
    hanoi(a-1, mid, start, end)

print(pow(2, n)-1)
if n <= 20:
    hanoi(n, 1, 2, 3)
