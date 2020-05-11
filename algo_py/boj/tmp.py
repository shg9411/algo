n=int(input())


for i in range(1, n+1):
   
   a=list(map(int,input().split()))
   sum=0
   avg=0
   
   count=0
   for j in range(1,len(a)):
      sum+=a[j]
     
   
   avg=sum/(len(a)-1)
   
   
  
   
   for p in range (1,len(a)):
      
      
      if int(a[p])>avg :
         count+=1
      
      
      
   print("%.3f%%" % (count/a[0]*100))
   
