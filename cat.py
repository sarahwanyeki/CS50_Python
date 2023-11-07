# while do the code again and again but leaves the particulars 
# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1 # assignment operator copies from right to left


#the same thing but shortend
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


#for Loop and List(type of data)
# For loops helps to iterate over a list of items

# for i in [0, 1, 2]: # bracket rep a list
#     print("meow")

#the better way is using a function range
# for i in range(10): # this is a function
#     print("meow")


#the better pythonic
# for _ in range(4): #using underscore is declaring a variable and because you won't use it later
#     print("meow")

 
# print("meow\n" * 3, end="") # another way of running the same thing


#only until the user gives you a value
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")
       

# # meow function
# def main():
#     meow(3)


# def meow(n):
#     for _ in range(n):
#         print("meow")


# main()

# meow function that user inserts number
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
             break
    return n

def meow(n):
    for _ in range(n):
        print("meow")


main()