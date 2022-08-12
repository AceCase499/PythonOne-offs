def rev_sentence(usersent):
    usersent = usersent.split()
    counter = -1

    for i in usersent:
        print(usersent[counter])
        counter = counter - 1


def main():
    user_sentence = input("Enter a String sentence: ")
    rev_sentence(user_sentence)


main()
