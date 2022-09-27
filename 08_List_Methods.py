# List Methods 

# List slicing 
friends = ["Emon", "Ankit", "Rohan", 465]
print(friends[0:2])

# Sorting methods 
l1 = [1,2,45,5,6,8,21] 
l1.sort() #The list is sorted from low to bigger/larger
print(l1)
l1.reverse() # Reverses the List 
print(l1)

l1.append(45) #Appends at the end of the list
print(l1)
# Always remeber list.append() adds at the end 
l1.insert(1,544) #This updates/adds 544 at the index of 1. At the original list. 
#The list is now something like this 
# [1, 544, 2, 45, 5, 6, 8, 21]
print(l1)  #Which can be verfied here 
l1.pop(2) #It removes the elemment at index 2 
print(l1)

l1.remove(21) #It removes 21 from the list l1
print(l1)

# Append is the most usefull method of List in Python 
