import random


def generate_numbers(count):
    my_list = random.sample(range(1, 101), count)  # creates a list of 10 randomly selected ints between 1 and 100
    print(my_list)
    return my_list


def main():
    my_list = generate_numbers(10)
    print("Example built-in list functions:")
    print("Sum of the numbers:  ", sum(my_list))  # DO NOT USE for assignment 1
    print("Max of the numbers:  ", max(my_list))
    print("Min of the numbers:  ", min(my_list))
    print("Index of min of the numbers:  ", my_list.index(min(my_list)))
    my_list.insert(1, 15)
    print("15 inserted at index 1: ", my_list)
    print("Sorted list will look like: ", sorted(my_list))
    print("Remove the last number from the last: ", my_list.pop())
    my_list.reverse()
    print("Reversed list: ", my_list)


main()
