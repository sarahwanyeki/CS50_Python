def main():
    face = input("Enter Your Face: ")
    print("you have a", convert(face), "face" )


def convert(face):
    happy_face = face.replace(":)", "🙂" )
    sad_face = happy_face.replace(":(", "🙁")
    return sad_face
    

main()