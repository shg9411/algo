def solution(a, b, budget):
    if a < b:
        b, a = a, b
    count = 0
    bigCount = budget // a

    while bigCount >= 0:
        tmp = budget - bigCount*a
        if tmp == 0:
            count += 1
        else:
            smallCount = tmp // b
            if tmp == smallCount * b:
                count += 1
        bigCount -= 1
    return count


print(solution(3000, 5000, 1000000))
