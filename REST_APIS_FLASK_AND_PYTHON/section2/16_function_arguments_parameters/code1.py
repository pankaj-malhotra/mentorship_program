def add(x, y):
    result = x + y
    print(result)

add(5, 3)

def say_hello():
    print("Hello!")

say_hello()

def say_hello(name):
    print(f"Hello, {name}")

say_hello("Bob")

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("Bob", "Smith")
say_hello(surname="Bob", name="Smith")

def divide(divident, divisor):
    if divisor !=0 :
        print(divident / divisor)
    else:
        print("You fool!")

divide(15, 0)
divide(divident=15, divisor=3)
