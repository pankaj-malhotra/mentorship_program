Tuple1 = ()
print("\nInitial empty tuple:")
print(Tuple1)

Tuple1 = ('Geeks', 'For', 'Geeks')
print("\nTuple with the use of string:")
print(Tuple1)

list1 = [1, 2, 4, 5, 6]
print("\nList:", list1)
print("\nTuple using list:")
print(tuple(list1))

Tuple1 = tuple('Geeks')
print("\nTuple with the use of function:")
print(Tuple1)

Tuple2 = ('Geeks')
print("\nTuple:", Tuple2)

Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes:")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples:")
print(Tuple3)

Tuple1 = ('Geek',) * 3
print("\nTuple with repetition:")
print(Tuple1)

Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop:")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

Tuple2 = ("Geeks", "For", "Geeks")

for i in range(0, len(Tuple2)):
    print(Tuple2[i])

Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple:")
print(Tuple1[1])

Tuple1 = ("Geeks", "For", "Geeks")

a, b, c = Tuple1
print("\nValues after unpacking:")
print(a)
print(b)
print(c)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2

print("Tuple 1:")
print(Tuple1)

print("\nTuple2:")
print(Tuple2)

print("\nTuples after concatenation:")
print(Tuple3)

Tuple1 = tuple('GEEKSFORGEEKS')
print("Removal of First element:")
print(Tuple1[1:])

print("\nTuple after sequence of element is reversed:")
print(Tuple1[::-1])

print("\nPrinting elements between range 4-9:")
print(Tuple1[4:9])

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

#print(Tuple1)


Tuple1 = ('Geeks', 'For', 'Geeks')

for i in range(0, len(Tuple1)):
    print(Tuple1[i])

for i in Tuple1:
    print(i)