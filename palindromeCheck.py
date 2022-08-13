def createalphastring(string):
    charlist = []
    for i in range(len(string)):
        if string[i].isalpha():
            charlist.append(string[i].lower())
    return charlist


def isPalindrome(string):
    charList = createalphastring(string)
    palindrome = True
    half = int(len(charList) / 2)
    for i in range(half):
        if charList[i] != charList[(-i - 1)]:
            palindrome = False
    return palindrome


def main():
    string = input('Enter a string ')
    charList = createalphastring(string)

    if isPalindrome(charList):
        print(string + " is a Palindrome")
    else:
        print(string + " is not Palindrome")


main()
