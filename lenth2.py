list1=[int(x) for x in input("enter the first list").split()]
list2=[int(x) for x in input("enter the second list").split()]
print("first list:",list1)
print("second list:",list2)
if len(list1)==len(list2):
 print("same length")
else:
 print("not same sum")
if sum(list1)==sum(list2):
 print("same sum")
else:
 print("Not same sum")
common=set(list1) & set(list2)
if common:
 print("common values:",common)
else:
 print("No common values:")
