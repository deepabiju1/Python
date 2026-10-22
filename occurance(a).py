names=[]
n=int(input("enter the no of names"))
for i in range(n):
  names.append(input("enter the names:"))
count=0
for name in names:
      count+=name.lower().count('a')
print("the occuranceof 'a'=",count)
