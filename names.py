# names = []


# for _ in range (3): # i or _ mean the same
#   name = input("What's your name? ")
#   names.append(name)  

# for name in sorted(names):
#     print(f"hello, {name}")


#file I/O saving the terminal output
# names = []

# name = input("What's your name? ")
# file = open("names.txt", "w") #"w" rewrites the code
# file.write(name)
# file.close()
    
# name = input("What's your name? ")
# file = open("names.txt", "a") #"a" appends the names
# file.write(name)
# file.close()



#How to add a new line
# name = input("What's your name? ")

# file = open("names.txt", "a") #"a" appends the names
# file.write(f"{name}\n") #append in a new line
# file.close()


#more pythonic to close the file without using close

# name = input("What's your name? ")

# with open("names.txt", "a") as file: #"with" closes the file and saves it
#     file.write(f"{name}\n") #append in a new line



########## Read File ###############
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip()) #rstrip is used to remove extra lines


###### removing many lines of code #########
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())


######## sort the names before printing ############
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) #rstrip removing the whitespace 

for name in sorted(names):
    print(f"hello, {name}")