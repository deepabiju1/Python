s=input("enter the string:")
first=s[0]
result=first+s[1:].replace(first,"$")
print(result)
