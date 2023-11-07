def main():
    x = int(input("What is x? "))
    if is_parity():
        print("Even")
    else:
        print("Odd")

def is_parity(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()

    

   


