def solution(money, expected, actual):
    answer = -1
    base = 100
    cur = base
    for expect,real in zip(expected,actual):
        if expect==real:
            money+=cur
            cur=base
        else:
            money-=cur
            cur = min(money,cur*2)
            if money==0:
                break
    return money