# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])

# #trex
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])


# use function from another file
import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])