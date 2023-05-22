def revString(textt, rev):
    if textt == "":
        return rev

    erse = textt[0] + rev
    return revString(textt[1:], erse)


def main():
    print(revString("Octopus", ""))


main()
