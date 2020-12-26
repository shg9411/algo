def solution(n):
    if n % 5 == 0:
        return n//5
    five = n//5
    for i in range(five, -1, -1):
        if (n-(i*5)) % 3 == 0:
            return i+(n-(i*5))//3
    return -1


print(solution())
