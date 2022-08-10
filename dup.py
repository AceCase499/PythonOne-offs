def dupe(lst1, lst2):
    for l1 in lst1:
        for l2 in lst2:
            if l1 == l2:
                return True
    return False


def main():
    listOne = [90, 80, 70, 60]
    listTwo = [11, 22, 33, 44]
    listThree = [1, 2, 3, 4]
    listFour = [1, 2, 3, 4]

    print(dupe(listThree, listTwo))


main()
