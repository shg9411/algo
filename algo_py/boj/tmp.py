d = 0
def backtracking(k,num):
    global Min,Max,d
    d+=1
    if k == N-1:
        if num < Min:
            Min = num
        if num > Max:
            Max = num
        return
    for i in range(N-1):
        if chk[i]: continue
        chk[i] = 1
        if cal[i] == '+':
            backtracking(k+1, num+A[k+1])
        elif cal[i] == '-':
            backtracking(k+1, num-A[k+1])
        elif cal[i] == '*':
            backtracking(k+1, num*A[k+1])
        else:
            if num < 0:
                backtracking(k+1, -((-num)//A[k+1]))
            else:
                backtracking(k+1, num//A[k+1])
        chk[i] = 0

N = int(input()) #수의 개수
A = list(map(int,input().split())) #[A1, A2, ... An]
cnt = list(map(int,input().split())) #[2,1,1,1]
chk = [0] * (N-1) #[0,0,0,0,0]
cal = ['+']*cnt[0] + ['-']*cnt[1] + ['*']*cnt[2] + ['%']*cnt[3] #['+','+','-','*','%']
Max = -987654321;Min = 987654321
backtracking(0,A[0])
print(Max,Min,sep="\n")
print(d)