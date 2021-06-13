n, m = map(int, input().split())
lessons = list(map(int, input().split()))
subtotal = [lessons[0]]
for lesson in lessons[1:]:
    subtotal.append(subtotal[-1]+lesson)
l = max(lessons)
r = subtotal[-1]
ans = r


def can(val):
    tmp = 0
    cnt = 1
    i = 0
    while i < n:
        if subtotal[i] - tmp > val:
            if (cnt := cnt+1) > m:
                return False
            tmp = subtotal[i-1]
        i += 1
    return True


while l <= r:
    mid = (l+r)//2
    if can(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid+1
print(ans)
