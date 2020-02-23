N=int(input())
cnt=0
for n in range(N):
    word=input()
    ls=[]
    flag=False
    while flag!=True:
        n=len(word)
        if n==1:
            if word not in ls:
                cnt+=1
                flag=True
                break
            else:
                flag=True
                break
        else:
            for i in range(n):
                if word[i] in ls:
                    flag=True
                    break
                elif word[i+1]==word[i]:
                    continue
                elif word[i+1]!=word[i]:
                    ls.append(word[i])
                    word=word[i+1:]
                    break
print(cnt)