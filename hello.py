# #Ask user their name
# name=input("What is Your Name? ")

# print("Hello, " + name)

#Ask user their name
# name=input("What is Your Name? ")

# print("Hello, " + name)

# name=input("What is Your Name? ")

# print("Hello, ", end="")
# print(name)

# name=input("What is Your Name? ")  

# print("Hello,", name, sep="???")

# print('hello, "Friend')

# How to use f for format and ginger (curly braces) to call our variable
# name=input("What is Your Name? ")

# print(f"Hello, {name}") # f explains to python to speacial format

# name=input("What is Your Name? ")
# name = name.strip()
# print(f"Hello, {name}") 

# name=input("What is Your Name? ")

# Remove whitesapce from str
# name = name.strip()

# #Capitalize user's name
# name = name.title()

# Remove whitesapce from str And capitalize users name
# name = name.strip().title()
#f special format


# #shoten the code of line 
# name=input("What is Your Name? ").strip().title()
# #f special format
# print(f"Hello, {name}") 



name = input("What is Your Name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

#f special format
print(f"Hello, {last}") 