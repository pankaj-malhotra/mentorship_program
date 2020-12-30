class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        total = 0
        for item in self.items:
            total = total + item['price']
        return total

    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + " - franchise")
        return new_store

    @staticmethod
    def store_details(store):
        #return f"{store.name}, total stock price: {store.stock_price}"
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

store = Store("Test")

store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store)
Store.franchise(store2)

Store.store_details(store)
Store.store_details(store2)


print(store)
print(store2)
