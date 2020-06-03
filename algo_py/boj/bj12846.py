def solve():
    n = int(input())
    maxPay = 0
    pay = [0] + list(map(int, input().split())) + [0]
    stack = [0]
    for i in range(1, len(pay)):
        while stack and pay[stack[-1]] > pay[i]:
            val = stack.pop()
            x = i-1-stack[-1]
            tmpPay = x * pay[val]
            if tmpPay > maxPay:
                maxPay = tmpPay
        stack.append(i)
    print(maxPay)


if __name__ == '__main__':
    solve()
