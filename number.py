# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("X is not an integer")
# else:
#     print(f"x is {x}")

# allow user to insert the correct number
while True:
    try:
        x = int(input("What's X? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
