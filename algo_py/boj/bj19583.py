import sys


def totime(x):
    h, m = map(int, x.split(":"))
    return h*60+m


s, e, q = map(totime, input().split())
present = set()
res = 0
for log in sys.stdin.read().splitlines():
    try:
        time, person = log.split()
        time = totime(time)
        if time <= s:
            present.add(person)
        elif e <= time <= q:
            if person in present:
                res += 1
                present.remove(person)
        if time > q:
            break
    except:
        pass
print(res)
