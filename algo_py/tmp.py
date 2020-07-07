N = int(input())
cycle =0
N_Orig = N

while True:  
    print(N)
    if N>10: 
        N = str(N) 
        N_0 = int(N[1])*10 
        N_1 = int(N[0])+int(N[1]) 
        if N_1 > 10 :
            N_1 = int(str(N_1)[1])
        N = N_0 + N_1 
    
  
    else : 
        N = str(N) 
        N_0 = 0
        N_1 = int(N[0]) 
        N = N_0 + N_1 
    
    cycle += 1

    if N_Orig==N:
        break

print(cycle)    
