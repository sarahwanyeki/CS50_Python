# students = ["Sarah", "Lucy", "Ron"]

# for student in students: # for loop to iterate a list
#     print(student)

# iterate using numbers
students = ["Sarah", "Lucy", "Ron"]

for i in range(len(students)): # range works with interger, len works with list and str
    print(i + 1, students[i]) # added +1 so that it can start from 1 not 0
    