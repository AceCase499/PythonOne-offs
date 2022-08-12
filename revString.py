def revString(str, n):
    chrs = 0
    for i in str:
        chrs += 1

    if n == chrs:
        return
    else:
        revString(str, n+1)
    print(str[n])


def main():

    print(revString("Elephant", 0))


main()
