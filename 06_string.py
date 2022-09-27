# # a = 34 


name = "soumya"
# # print(type(a)) #It will print int 
# # print(type(name)) #It will print string

# greeting = "Good Morning"
# # concatinating two strings
# print(greeting+ ' '+name) #to add the strings 

print(name[0]) #it will return s as this is the first char of the name string 
# Note as the the lenght of the name string is 6  so it can be printed to length -1 
# as computer starts counting from 0
# Next the print(name[5]) will return the 'a' character 

# Slicing 
print(name[0:3]) #it will return sou to the 2nd character like s-0, o-1, u-2
print(name[1:4]) #its gonna be returning oum


print(name[:4]) # is same as name[0:4]
print(name[0:]) # is same as name[0:5]

# Negative indices
# The indes in a string starts from o to (length -1 ) in python. In order to slice a string , we use the following 
# syntax 
c = name[-4:-1] #is same as name[0:4]
print(c)

# Slicing with skip value
# we can provide a skip value as a part of our slice like this 
d = name[1:4:2] #it will skip all the 2nd characters 
print(d)

# string functions in python
story = "hello world ap badhiya ho!"
print(len(story)) # to get the length of story 
print(len(name))
print(story.endswith("ho!")) #it will return true
print(story.count("a")) #return 3 
print(story.capitalize())
print(story.find("ap")) #give the first occurance only 
print(story.replace("ap", "tum")) #to replace ap with tum. It changes all the occurancces

# Escape sequence 
story2 = "Soumyajit is a \n very good boy"
print(story2)

# There are some escape sequence character what we learn in future also 
# the \n is the most used one 

# Examples : \n : newline, 
#           \t : tab,
#           \' : single quote,
#           \\: backslash etc. 

# String chapter ends