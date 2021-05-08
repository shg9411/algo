def solution(n, k, cmd):
    f_t = [0 for _ in range(n+1)]
    v_t = [0]+[1 for _ in range(n)]

    def sum(i):
        res = 0
        while i > 0:
            res += f_t[i]
            i -= (i & -i)
        return res

    def update(i, diff):
        while i <= n:
            f_t[i] += diff
            i += (i & -i)

    for i in range(1, n+1):
        update(i, 1)
    deleted = []
    cur = k+1
    for line in cmd:
        if line == 'C':
            deleted.append(cur)
            update(cur, -1)
            v_t[cur] = 0
            if sum(n)-sum(cur) > 0:
                for i in range(cur+1, n+1):
                    if v_t[i] == 1:
                        cur = i
                        break
            else:
                for i in range(cur-1, 0, -1):
                    if v_t[i] == 1:
                        cur = i
                        break
        elif line == 'Z':
            r = deleted.pop()
            update(r, 1)
            v_t[r] = 1
        else:
            md, c = line.split()
            c = int(c)
            sumCur = sum(cur)
            if md == 'D':
                s = cur+1
                e = n
                while s <= e:
                    m = (s+e) >> 1
                    v = sum(m)-sumCur
                    if v < c:
                        s = m+1
                    elif v > c:
                        e = m-1
                    else:
                        for i in range(m, s-1, -1):
                            if v_t[i] == 1:
                                cur = i
                                break
                        break
            else:
                s = 1
                e = cur-1
                while s <= e:
                    m = (s+e) >> 1
                    v = sumCur-sum(m)
                    if v < c:
                        e = m-1
                    elif v > c:
                        s = m+1
                    else:
                        for i in range(m, s-1, -1):
                            if v_t[i] == 1:
                                cur = i
                                break
                        break
    answer = ''.join(('O' if v_t[i] else 'X' for i in range(1, n+1)))
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))
