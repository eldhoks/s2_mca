def factorial_recursive(n):
 if n==0 or n==1:
  return 1
 else:
  return n*factorial_recursive(n-1)
#input from th user
num=int(input("enter the number:"))
result=factorial_recursive(num)
print'the factorial of {0} is'.format(num),result
