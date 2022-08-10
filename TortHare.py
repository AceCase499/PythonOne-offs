def findDuplicate(nums):
    turtle = nums[0]
    hare = nums[0]
    while True:
        turtle = nums[turtle]
        hare = nums[hare]
        if turtle == hare:
            break

    ptr1 = nums[0]
    ptr2 = turtle
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


def main():
    print(findDuplicate([3, 1, 3, 4, 2]))


main()
