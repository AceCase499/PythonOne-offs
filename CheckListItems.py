def comparelistno(the_list, n):
    less_count = 0
    for i in the_list:
        if i < n:
            less_count += 1
    return less_count


def main():
    this_list = [40, 4, 14, 7, 89, 44, ]
    result = comparelistno(this_list, 15)
    print(result)


main()
