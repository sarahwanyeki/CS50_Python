# x = float(input("what's x? "))
# y = float(input("what's y? "))

# z = round(x + y)
# print(f"{z:,}") # special format and insert comma separator for thousands

# z = round(x / y, 2)
# print(z)

# z = x / y
# print(f"{z:.2f}") # the way you specify using f how many digits you want to use



#test Unit
def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
