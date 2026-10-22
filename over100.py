num=input("enter integers seperated by spaces:").split()
result=['over' if int(x)>100 else int(x) for x in num]
print("result:",result)
