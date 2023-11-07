# x = int(input("What's is x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# create my own function to determine even and odd numbers
# def main():
#     x = int(input("What's is x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0: 
#         return True
#     else:
#         return False
# main()

#pythonic way of rewriting the above code
# def main():
#     x = int(input("What's is x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return True if n % 2 == 0 else False
# main()

#simplify it even better
def main():
    x = int(input("What's is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0
main()
