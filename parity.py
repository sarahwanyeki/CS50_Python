# x = int(input("What's is x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# create my own function to determine even and odd numbers
def main():
    x = int(input("What's is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()

