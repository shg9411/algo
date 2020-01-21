import sys
sys.setrecursionlimit(10**6)

startpointlocation=[[0,0]]*5001
for i in range(1, 5001):
    startpointlocation[i]=[i,i-1]

startpointvalue=[1]
for i in range(1,5001):
    startpointvalue.append(pow((2*(i-1))+1,2)+1)

def findshellnum(r,loc):
    if loc[0]==0 and loc[1]==0:
        return 1

    shellnum=startpointlocation[r].copy()
    shellcount = startpointvalue[r]

    
    for i in range(2*r-1):
        if loc[0]==shellnum[0] and loc[1]==shellnum[1]:
            return shellcount
        shellnum[1]-=1
        shellcount+=1

    for i in range(2*r):
        
        if loc[0]==shellnum[0] and loc[1]==shellnum[1]:
            return shellcount
        shellnum[0]-=1
        shellcount += 1

    for i in range(2 * r):
        if loc[0]==shellnum[0] and loc[1]==shellnum[1]:
            return shellcount
        shellnum[1]+=1
        shellcount += 1

    for i in range(2 * r+1):
       
        if loc[0]==shellnum[0] and loc[1]==shellnum[1]:
            return shellcount
        shellnum[0]+=1
        shellcount += 1

r1,c1,r2,c2=map(int,input().split())

biggestshellnum=0
for j in range(r1,r2+1):
    for i in range(c1,c2+1):
        whichshell = max(abs(i), abs(j))
        shellnum=findshellnum(whichshell,[i,j])
        #print("shellnum=",shellnum)

        #print(biggestshellnum,shellnum)
        if biggestshellnum<shellnum:
            biggestshellnum=shellnum

cnt=1
while True:
    if biggestshellnum//pow(10,cnt)==0:
        break
    cnt+=1

res=''

for j in range(r1,r2+1):
    for i in range(c1,c2+1):
        whichshell1 = max(abs(i), abs(j))
        res += '%' + str(cnt) + 's'
        res =res % findshellnum(whichshell1,[i,j])
        if i!=c2:
            res+=' '

    if j!=r2:
        res+='\n'

print(res)