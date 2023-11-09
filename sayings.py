def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name} ")



def goodbye(name):
    print(f"goodbye, {name}")


# let us avoid calling main on a different file if we dont have to use it
if __name__ =="__main__": #then and only then would you actually call main
    main()

