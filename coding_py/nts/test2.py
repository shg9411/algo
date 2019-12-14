def solution(n):
    count = 0
    numset = list(map(int, set(str(n))))
    for num in numset:
        if num == 0:
            continue
        if n % num == 0:
            count += 1
    return count


solution(1234)
