def solution(S):
    tmp = S
    for c in range(0,len(S)):
        tmp = min(S[:c]+S[c+1:],tmp)
    return tmp