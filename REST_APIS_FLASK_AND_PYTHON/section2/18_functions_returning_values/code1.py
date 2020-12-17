def add(x, y):
    print(x + y)
    return x + y

add(5, 8)
result = add(5, 8)
print(result)
print()

def add1(x, y):
    print(x+y)

print(add1(5, 8))
print()

def add2(x, y):
    return
    print(x + y)
    return x + y

result = add2(5, 8)
print(result)
print()

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 0) * 5
print(result)
