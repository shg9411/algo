def solution(n):
    answer = bin(n)[2:]
    tmp = answer.count('1')
    for i in range(n+1,1000001):
        if bin(i)[2:].count('1')==tmp:
            return i
