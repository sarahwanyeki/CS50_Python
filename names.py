names = []


for _ in range (3): # i or _ mean the same
  name = input("What's your name? ")
  names.append(name)  

for name in sorted(names):
    print(f"hello, {name}")


#file I/O saving the terminal output