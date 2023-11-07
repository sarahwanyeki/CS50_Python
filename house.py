# name = input("What's your name? ")

# if name == "Sarah":
#     print("Sobea")
# elif name == "Lucy":
#     print("Sobea")
# elif name == "Josphat":
#     print("Sobea")
# elif name == "Kare":
#     print("Milimani")
# else:
#     print("Who?")

# #Clean the code
# name = input("What's your name? ")

# if name == "Sarah" or name == "Lucy" or name == "Josphat":
#     print("Sobea")  
# elif name == "Kare":
#     print("Milimani")
# else:
#     print("Who?")

#use match as case
name = input("What's your name? ")

match name:
    case "Sarah":
        print("Sobea")
    case "Lucy":
        print("Sobea")
    case "Josphat":
        print("Sobea")
    case "Kare":
        print("Milimani")
    case _: #underscore showing anything that hasn't been defined
        print("who?")    
