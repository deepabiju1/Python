num =int(input("enter the number to find factorial"))
factorial=1
if(num<0):
  print("sorry factorial doesnot exit for negative numbers")
elif(num==0):
  print("the factorial of 0 is 1")
else:
 for i in range(1,num+1):
  factorial=factorial*i
print(" factorial of thegiven numbers",num,"is",factorial)
