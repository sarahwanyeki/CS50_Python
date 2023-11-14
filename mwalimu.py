# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")



# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")



######## create a get_student function to call get_name $ get_house
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #### return multiple values which is a tuple

if __name__ == "__main__":
    main()