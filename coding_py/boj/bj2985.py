n, m, k = input().split()
exp = ['==','+','-','*','/']

for q in exp:
    for w in exp:
        exec('tmp=eval(n+q+m+w+k)')
        if type(tmp)==bool and tmp==True:
            t = n+q+m+w+k
            t = t.replace('==','=')
            print(t)
            exit()
        