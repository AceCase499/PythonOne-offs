
# def vendingMachine(num_items, item_price):
class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def set_num_items(self, num_items):
        self.num_items = num_items

    def get_num_items(self):
        return self.num_items

    def set_item_price(self, item_price):
        self.item_price = item_price

    def get_item_price(self):
        return self.item_price

    def buy(self, req_items, money):  # req_items = # of items, money = amount of money user enters
        bill = req_items * VendingMachine.get_item_price(self)
        try:
            if self.get_num_items() < req_items:
                raise ValueError("Not enough items in the machine.")
        except ValueError as greedyError:
            print(greedyError)
            return 0
        try:
            if bill > money:
                raise ValueError("Not enough coins.")
            else:
                self.set_num_items(self.get_num_items() - req_items)
                print("You successfully purchased ", req_items, " items.")
        except ValueError as poorError:
            print(poorError)
            return 0
        return money - bill


def main():
    shop = VendingMachine(30, 5)
    print(shop.buy(3, 16))
    print("Stock Remaining: ", shop.get_num_items())


main()
