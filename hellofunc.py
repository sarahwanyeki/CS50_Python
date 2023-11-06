# def hello():
#     print("hello")
    
# name = input("what's is your name? ")
# hello()
# print (name)

# passing parameters in a function  and printing it in one line
# def hello(to):
#     print("hello,", to)
    
# name = input("what's is your name? ")
# hello(name) # calling function with an argument


def hello(to="world"):
    print("hello,", to)

hello()    
name = input("what's is your name? ")
hello(name) # calling function with an argument