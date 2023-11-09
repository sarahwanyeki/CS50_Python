# import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndentationError:
#     print("Too few arguments")


#Slice subset of a list
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

