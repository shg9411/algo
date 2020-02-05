word = list(input())
count = 0
top = 0

while (top < len(word)):
    if(word[top]=='c' and top+2<len(word) and (word[top+1]=='-' or word[top+1]=='=')):
        count += 1
        top += 2
    elif(word[top]=='d' and top+2<len(word) and word[top+1]=='z' and word[top+2]=='='):
        count += 1
        top += 3
    elif(word[top]=='d' and top+1<len(word) and word[top+1]=='-'):
        count += 1
        top += 2
    elif(word[top]=='l' and top+1<len(word) and word[top+1]=='j'):
        count += 1
        top += 2
    elif(word[top]=='n' and top+1<len(word) and word[top+1]=='j'):
        count += 1
        top += 2
    elif(word[top]=='s' and top+1<len(word) and word[top+1]=='='):
        count += 1
        top += 2
    elif(word[top]=='z' and top+1<len(word) and word[top+1]=='='):
        count += 1
        top += 2
    else:
        count += 1
        top += 1
        
print(count)