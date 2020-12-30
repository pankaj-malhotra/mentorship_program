class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)

    def __str__(self):
        return f"'{self.name}': {self.items}"

    def stock_price(self):
        total = 0
        for item in self.items:
            print("item :", item)
            total = total + item['price']

        return total

    def stock_price1(self):
        return sum([item['price'] for item in self.items])


store = Store("Fruits")
store.add_item("Apple", 30)
store.add_item("Banana", 40)
store.add_item("Grapes", 25)

print(store)
print("Total Price :", store.stock_price())
print("Total Price :", store.stock_price1())

