# from calculator import square

# def main():
#     test_square()

# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")

# if __name__ == "__main__":
#     main()

#assert another way of testing code 

# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try: 
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was ot 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")

# if __name__ == "__main__":
#     main()



#reduce the number of code by catching the error and assert
# use of pytest library
#unit test test for functions that you have written
# from calculator import square


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square (-3) == 9
#     assert square(0) == 0