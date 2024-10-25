def fibanacci_iterative(n):
 fib_series=[]
 a,b=0,1
 for i in range(n):
  fib_series.append(a)
  a,b=b,a+b
 return fib_series
#input from user
num_terms=int(input("enter the no of terms:"))
result=fibanacci_iterative(num_terms)
print'the fibanacci series for {0} term is'.format(num_terms),result
