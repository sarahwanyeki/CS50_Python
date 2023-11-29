# word = "PyThOn"
# result = ""

# for i in word:
#     if i.islower():
#         result += i.upper()

# print(result)

# n = 10000
# count = 0
# while n:
#     count = count + 1
#     n = 10000//10

# print(count)

# word = "python"
# result = ""
# i=0

# while i < len(word):
#     result += word[i].upper()

#     i += 1

# print(result)

number = 1234567890
result = 0
i = 0

while number > 0:
    result += number % 10
    number //= 100

print(result)