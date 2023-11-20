# def main():

##### 1st method
    #name = get_name()
    # house = get_house()
##### 2nd Method using tuple
    # name , house = get_student()
    # print(f"{name} from {house}")
#### 3rd method using index
    # student = get_student()
    # print(f"{student[0]} from {student[1]}")

########### remove the name variable since we are using it once and use return
# def get_name():
#     name = input("name: ")
#     return name

# def get_name():
#     return  input("name: ")
    
# def get_house():
#    return input("House: ")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)


############   Dictionar Object with keys and Values ##########


# def main():

#     student = get_student()
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


# if __name__ == "__main__": ##### if the name of this file equals name then let us go ahead and call main
#     main()


######### Make changes in a dictionary #######
def main():
    student = get_student()
    if student ["name"] == "Sarah":
        student["house"] == "Miti Moja"
    print (f"{student['name']} from {student['house']}")

    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}



if __name__ == "__main__":
    main()

