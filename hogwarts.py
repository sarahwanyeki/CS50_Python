# students = ["Sarah", "Lucy", "Ron"]

# for student in students: # for loop to iterate a list
#     print(student)

# iterate using numbers
# students = ["Sarah", "Lucy", "Ron"]

# for i in range(len(students)): # range works with interger, len works with list and str
#     print(i + 1, students[i]) # added +1 so that it can start from 1 not 0


#Dictionaries are a data structure that allows you to associate one value with another
# keys and values
# students = {
#     "Sarah": "Sobea", 
#     "Lucy": "Sobea", 
#     "Kare": "Milimani", 
#     "Josphat": "Sobea"
#     }

# for student in students:
#     print(student, students[student], sep=", ")


#multiple values
students = [
    {"name": "Sarah", "house": "Sobea", "location": "Nakuru"},
    {"name": "Lucy", "house": "Sobea", "location": "Njoro"},
    {"name": "Kare", "house": "Milimani", "location": "Bahati"},
    {"name": "Josphat", "house": "Sobea", "location": None},

]

for student in students:
    print(student["name"], student["house"],  student["location"], sep=", ")