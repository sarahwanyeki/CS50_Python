import csv

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
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_name(student): #a function of returning a name so that we can sort the names with key
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")



#we can use a lambda function if we can only use a function onve
#lambda unoniymous function
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     #lambda student: students["name"] ######this line of code is equivalent to get_name function
#     print(f"{student['name']} is in {student['house']}")



#################### csv reader #################\
# you'll have to import csv
# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, location, home in reader:
#         students.append({"name": name, "location": location, "home": home})

    

# for student in sorted(students, key=lambda student: student["name"]):
#     #lambda student: students["name"] ######this line of code is equivalent to get_name function
#     print(f"{student['name']} is in {student['location']} at {student['home']}")



############################# use of dictreader
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:

#         students.append({"name": row["name"], "home": row["home"]}) #  

    

# for student in sorted(students, key=lambda student: student["name"]):
#     #lambda student: students["name"] ######this line of code is equivalent to get_name function
#     print(f"{student['name']}  is from  {student['home']}") #


################### write csv file #############  