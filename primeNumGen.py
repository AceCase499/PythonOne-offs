def prime_or_composite(n):
    has_divisor = False

    for i in range(2, n):
        if n % i == 0:
            has_divisor = True
    
    if has_divisor:
        print(n, "is a composite number.")
    else:
        print(n, "is not a composite number.")


def main():
    user_num = int(input("Enter an integer greater than 1: "))
    numbers = []
    for count in range(2, user_num + 1):
        numbers.append(count)

    for i in range(len(numbers)):
        prime_or_composite(numbers[i])


main()
