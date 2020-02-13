import itertools

def eratos(n):
    n = int(n)
    sieve = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    sieve[0],sieve[1] = False,False
    return sieve


def solution(numbers):
    numbers = sorted(list(numbers), reverse=True)
    sosu = eratos(''.join(numbers))
    tmp = set()
    for i in range(1,len(numbers)+1):
        for item in itertools.permutations(numbers,i):
            tmp.add(int(''.join(item)))
    answer = 0
    for item in tmp:
        if sosu[item]:
            answer+=1
    
    return answer


numbers = '011'
print(solution(numbers))
