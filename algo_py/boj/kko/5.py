def getTime(t):
    h, m, s = map(int, t.split(':'))
    return 3600*h+60*m+s


def toST(t):
    ans = ''
    th, tm = divmod(t, 3600)
    if th < 10:
        ans += '0'
    ans += str(th)+":"
    tm, ts = divmod(tm, 60)
    if tm < 10:
        ans += '0'
    ans += str(tm)+":"
    if ts < 10:
        ans += '0'
    ans += str(ts)
    return ans


def solution(play_time, adv_time, logs):
    pt = getTime(play_time)
    at = getTime(adv_time)
    if pt == at:
        return "00:00:00"
    time = []
    s = dict()
    e = dict()
    for log in logs:
        st, ed = map(getTime, log.split('-'))
        if st not in s:
            s[st] = 1
        else:
            s[st] += 1
        if ed not in e:
            e[ed] = 1
        else:
            e[ed] += 1
        time.append((st, ed))
    x = [0 for _ in range(pt+1)]
    cnt = s.get(0, 0)
    for i in range(1, pt+1):
        x[i] = x[i-1]+cnt
        if i in s:
            cnt += s[i]
        if i in e:
            cnt -= e[i]
    res = 0
    idx = 0
    time.sort()
    for i in range(pt+1-at):
        if res < x[i+at]-x[i]:
            idx = i
            res = x[i+at]-x[i]
    return toST(idx)


print(solution("02:03:55", "00:14:15", [
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

# okay
