import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndentationError:
    print("Too few arguments")
