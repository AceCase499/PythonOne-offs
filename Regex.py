import string
import re


# Write a Python code to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# Write a Python code that matches a string that has an x followed by four 'y'
# Write a Python code that matches a string that has an x followed by two to three 'y'.
# Write a Python code that matches a word containing 't'.
# Write a Python program where a string will start with the numbers 1, 2 or 3.


def problem1():
    print("Problem 1")
    Ustring = input("Enter a string: ")
    return re.search('\w', Ustring)


def problem2():
    print("Problem 2")
    Ustring = input("Enter a string: ")
    return re.search('xyyyy', Ustring)


def problem3():
    print("Problem 3")
    Ustring = input("Enter a string: ")
    return re.search('xy*', Ustring)


def problem4():
    print("Problem 4")
    Ustring = input("Enter a string: ")
    return re.search('t', Ustring)


def problem5():
    print("Problem 5")
    Ustring = input("Enter a string: ")
    return re.search('(1|2|3).*', Ustring)


def main():
    print(problem1())
    print(problem2())
    print(problem3())
    print(problem4())
    print(problem5())


main()
