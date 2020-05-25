stack=[]
while True:
    a=input().rstrip()
    if a=='.':
        break
    for i in range(len(a)):
        if a[i]=='(' or a[i]=='[':
            stack.append(a[i])
        if stack==[] and (a[i]==')' or a[i]==']'):
            stack.append(a[i])
        if stack!=[]:
            if (stack[-1]=='(' and a[i]==')') or (stack[-1]=='[' and a[i]==']'):
                stack.pop()
    
    if stack==[]:
        print('yes')
        
    if stack!=[]:
        print('no')
    stack=[]
   