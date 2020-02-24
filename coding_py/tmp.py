l = int(input())
text = input().rstrip()


modz = 100003


def mod(n):
    if n >= 0:
        return n % modz
    return ((-n//modz+1)*modz + n) % modz


low = 0
high = l
while low+1 < high:
    mid = (low+high)//2
    h = 0
    power = 1
    found = False
    catch = []
    for i in range(l-mid+1):
        if i == 0:
            for j in range(mid):
                h = mod(h+ord(text[mid-1-j])*power)
                if j < mid-1:
                    power = mod(power*2)
        else:
            h = mod(2*(h-ord(text[i-1])*power)+ord(text[i+mid-1]))

        if catch:
            for c in catch:
                same = True
                for j in range(mid):
                    if text[i+j] != text[c+j]:
                        same = False
                        break
                if same:
                    found = True
                    break
        if found:
            break
        else:
            catch.append(i)
    if found:
        low = mid
    else:
        high = mid
print(low)
