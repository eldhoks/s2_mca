n=int(input("enter the no of terms:"))
n1,n2=0,1
count=0
if(n<=0):
   print"please enter a positive number"
else: 
     print "fibanacci series upto",n
     while(count<n):
      print n1
      temp=n1+n2
      n1=n2
      n2=temp
      count+=1
     
    
