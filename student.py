
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return  input("Name: ")

# def get_house():
#     return  input("House: ")


# if __name__ == "__main__":
#     main()
    
# sample
# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")

# def get_student():
#     name1 = input("Name: ")
#     house1 = input("House: ")
#     return name1, house1



# if __name__ == "__main__":
#     main()


# #### Returning a Tuple & indexing into it ######
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return(name, house)


# if __name__ == "__main__":
#     main()



###### using dictionary for keys and values
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}") ### use single quote

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()

#### Clean The Code

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}") ### use single quote

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()