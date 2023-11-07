# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("X is not an integer")
# else:
#     print(f"x is {x}")

# allow user to insert the correct number
# while True:
#     try:
#         x = int(input("What's X? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")


# #myfunction
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's X? "))
#             return x
#         except ValueError:
#             print("x is not an integer")

# main()       


#myfunction and pass (silently ignore)
def main():
    x = get_int("What's X? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x # you can avoid using x variable if you aren't goint to use it again
            #return = int(input("What's X? "))       
        except ValueError:
           # print("x is not an integer")
           pass

main()
