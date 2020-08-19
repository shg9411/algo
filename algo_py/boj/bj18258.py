import sys
from collections import deque
q = deque()
res = []
for tmp in sys.stdin.read().splitlines():
    tmp = tmp.split()
    if tmp[0][-1]=='h':
        q.append(tmp[1])
    elif tmp[0][0]=='f':
        res.append(q[0] if q else '-1')
    elif tmp[0][-1]=='p':
        res.append(q.popleft() if q else '-1')
    elif tmp[0][0]=='s':
        res.append(str(len(q)))
    elif tmp[0][0]=='e':
        res.append('0' if q else '1')
    elif tmp[0][0]=='b':
        res.append(q[-1] if q else '-1')
print('\n'.join(res))     