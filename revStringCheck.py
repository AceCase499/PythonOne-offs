'''
This code finds the reverse of a given string.
'''


def revstring(string):
    reversedStr = ''
    for i in range(1, len(string) + 1):
        reversedStr += string[-i]
    return reversedStr


'''
for i in range(len(string)-1, -1, -1):
    reversed += string[i]
'''


def isequal(string1, string2):
    if string1 == string2:
        return True
    else:
        return False


def main():
    string = input('Enter a string: ')
    string2 = input('Enter another string to test the first one: ')
    updated = revstring(string)
    print("Original string: " + string)
    print("Reversed srting: " + updated)
    if isequal(updated, string2):
        print(string + " is the reversed version of " + string2)
    else:
        print(string + " is NOT the reversed version of " + string2)


main()
