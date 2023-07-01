try:
    age = int(input("How old are you?: "))

    if age < 0 or age > 120:
        raise ValueError("Age range is invalid")
    else:
        print(f"You are {age} year(s) old.")

except ValueError as err:
    print(err)
