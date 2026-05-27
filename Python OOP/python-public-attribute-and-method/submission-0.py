class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


chips = StoreItem("Chips", 1.99) # Don't modify this line

#print(str(chips.name) + "\n" str(chips.price))
print(chips.name)
print(chips.price)

# TODO: Access the attributes of the chips object and display them