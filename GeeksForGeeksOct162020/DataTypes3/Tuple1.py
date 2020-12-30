Tuple1 = ()
print("Initial empty tuple :")
print(Tuple1)

Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String :")
print(Tuple1)

List1 = [1, 2, 4, 5, 6]
print("\nTuple using List :")
print(tuple(List1))

Tuple1 = tuple('Geeks')
print("\nTuple with the use of function :")
print(Tuple1)

Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with mixed datatypes :")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples :")
print(Tuple3)

Tuple1 = ('Geeks', ) * 3
print("\nTuple with repetition :")
print(Tuple1)

Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop :")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

Tuple1 = tuple("Geeks")
print("\nFirst element of Tuple :")
print(Tuple1[1])

Tuple1 = ("Geeks", "For", "Geeks")
a, b, c = Tuple1
print("\nValues after unpacking :")
print("a :", a)
print("b :", b)
print("c :", c)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
Tuple3 = Tuple1 + Tuple2

print("\nTuple1 :")
print(Tuple1)

print("Tuple2 :")
print(Tuple2)

print("Tuples after concatenation :")
print(Tuple3)

Tuple1 = tuple('GEEKSFORGEEKS')
print("\nRemoval of First element :")
print(Tuple1[1:])

print("Tuple after sequence of element is reversed :")
print(Tuple1[::-1])

print("Printing elements between range 4-9 :")
print(Tuple1[4:9])

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1
#print(Tuple1)

Tuple1 = ()
Tuple2 = ("Geeks", "For", "Geeks")
Tuple1 = Tuple2
#Tuple1.add("Geeks")

print("\nTuple1 :")
print(Tuple1)