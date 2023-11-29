def main():
    input_time = input("What time is it? ")

    ans = convert(input_time)
    
    
    if ans >= 7 and ans<= 8:
        print("Breakfast time")
    if ans >= 12 and ans <= 13:
        print("Lunch time")
    if ans >= 18 and ans <= 19:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    # convert hours and minutes to float then divide minutes by 60
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()


# def main():
#     answer = input("What time is it? ")

#     time = convert(answer)
#     if time >= 7 and time <= 8:
#         print("Breakfast time")
#     if time >= 12 and time <= 13:
#         print("Lunch time")
#     if time >= 18 and time <= 19:
#         print("Dinner time")

# def convert(time):
#     hours, minutes = time.split(":")
#     new_minutes = float(minutes) / 60

#     return float(hours) + new_minutes

# if __name__ == "__main__":
#     main()
