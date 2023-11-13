# with open("students.csv") as file:

#     for line in file:
#         row = line.rstrip().split(",") # split used to split a line of words with comma
#         print(f"{row[0]} is in {row[1]}")


# ######## clean it a bit #########
# with open("students.csv") as file:

#     for line in file:
#         name, location = line.rstrip().split(",")
#         print(f"{name} is in {location}")


###### 
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

    for student in students:
        print(f"{student['name']} is in {student['house']}")
