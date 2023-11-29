# Get user input
expression = input("Enter numbers: ")


# Convert this into variables
x, y, z = expression.split(" ")

# Change type of variables x and z to float
num1 = float(x)
num2 = float(z)

# Calculate the result
if y == "+":
    ans = num1 + num2
if y == "-":
    ans = num1 - num2
if y == "*":
    ans = num1 * num2
if y == "/":
    ans = num1 / num2

print(round(ans, 1))