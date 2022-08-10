# ♪♪♪
def main():
    username = input("♪ The Name Game ♪ ")
    altName = ""

    username = username.capitalize()
    if username[0] == "A" or username[0] == "E" or username[0] == "I" or \
            username[0] == "O" or username[0] == "U" or username[0] == "Y":
        username = username.lower()
        altName += "B" + username
        print(username, username, "Bo", altName, "-♪")
        altName = ""
        altName += "F" + username
        print("Banana Fanana Fo", altName, "-♪")
        altName = ""
        altName += "M" + username
        print("Me My Mo", altName, "-♪")
        print(username, "!!")
    else:
        altName += "B"
        for i in range(1, len(username)):
            altName += username[i]
        print(username, username, "Bo", altName, "-♪")
        altName = ""
        altName += "F"
        for i in range(1, len(username)):
            altName += username[i]
        print("Banana Fanana Fo", altName, "-♪")
        altName = ""
        altName += "M"
        for i in range(1, len(username)):
            altName += username[i]
        print("Me My Mo", altName, "-♪")
        print(username, "!!")


main()
