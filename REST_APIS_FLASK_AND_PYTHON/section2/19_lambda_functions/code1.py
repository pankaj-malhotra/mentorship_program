def add(x, y):
    return x + y

print(add(5,7))
print()

add1 = lambda x, y: x + y
print(add1(5, 7))
print()

print((lambda x,y: x + y)(5, 7))
print()

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [x * 2 for x in sequence]
print(sequence)
print(doubled)

doubled1 = [double(x) for x in sequence]
print(doubled1)

doubled2 = list(map(double, sequence))
print(doubled2)

doubled3 = [(lambda x: x * 2)(x) for x in sequence]
print(doubled3)

doubled4 = list(map(lambda x: x * 2, sequence))
print(doubled4)
