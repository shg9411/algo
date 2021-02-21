import sys


def solve():
    q = [0]*2000000
    front = rear = 0
    res = []
    for string in sys.stdin.read().splitlines()[1:]:
        t = string[1]
        if t == "u":
            q[rear] = string[5:]
            rear += 1
        elif t == "o":
            if front == rear:
                res.append('-1')
            else:
                res.append(q[front])
                front += 1
        elif t == "i":
            res.append(str(rear-front))
        elif t == "m":
            res.append('1' if front == rear else '0')
        elif t == "r":
            res.append(q[front] if front != rear else '-1')
        elif t == "a":
            res.append(q[rear-1] if front != rear else '-1')

    sys.stdout.write('\n'.join(res))


if __name__ == '__main__':
    solve()
