def takeinput():
    sales = [0] * 7  # new list made of 7 '0' values
    for i in range(7):
        sales[i] = float(input("Enter the sale:"))
    return sales


def main():
    print("This program calculates the total sales for this week.")
    sales = takeinput()
    print("The total sales of the week:", sum(sales))


main()
