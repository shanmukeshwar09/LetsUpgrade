# Python program to Remove empty List from List 

myList = [5, 6, [], 3, [], [], 9] 

print("The original list is : " + str(myList))

res = [ele for ele in myList if ele != []] 

print ("List after empty list removal : " + str(res))
