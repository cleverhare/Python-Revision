# Problem 1 of the strings chapter
name = input("Enter your name: ")
date = input("Enter the date: ")
print("Good afternoon: "+name)

# Problem 2 
letter = '''Dear <|name|>
You're selected
Date: <|date|>'''

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)

print(letter)

#Problem 3 
str = "This is string   with double spaces"
something = str.replace("  ", " ")
print(something)

