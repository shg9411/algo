S = input()
result = list()

if '<' not in S:
    S = S.split(' ')
    for s in S:
        result.append(s[::-1])
    print(' '.join(result))

else:
    start_index = 0
    for i in range(len(S)):
        if S[i] =='<':
            if i!=0:
                result.append(S[i-1:start_index:-1])
            start_index = i
        if S[i] =='>':
            result.append(S[start_index:i+1])
            start_index = i
            
    if len(''.join(result))!=len(S):
        result.append(S[:start_index:-1])
    print(''.join(result))