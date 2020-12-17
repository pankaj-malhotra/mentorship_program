set1 = set()
print("Initial blank Set : ")
print(set1)

set1 = set("GeeksForGeeks")
print("\nSet with the use of String : ")
print(set1)

String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object : ")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List : ")
print(set1)

set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers : ")
print(set1)

set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values : ")
print(set1)

set1 = set()
print("Initial blank set : ")
print(set1)

set1. add(8)
set1. add(9)
set1. add((6, 7))
print("\nSet after Addition of Three elements : ")
print(set1)

for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5 : ")
print(set1)

set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using update : ")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)

print("\nElements of set : ")
for i in set1:
    print(i, end=" ")
print()

print("Geeks" in set1)
print()

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial Set : ")
print(set1)

set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements : ")
print(set1)

set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements : ")
print(set1)

for i in range(1, 5):
    set1.remove(i)

print("\nSet after Removing a range of elements : ")
print(set1)
print()

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial Set : ")
print(set1)

set1.pop()
print("\nSet after popping an element : ")
print(set1)
print()

set1 = set([1, 2, 3, 4, 5])
print("\nInitial Set : ")
print(set1)

set1.clear()
print("\nSet after clearing all the elements : ")
print(set1)
print()

String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
Fset1 = frozenset(String)
print("The FrozenSet is : ")
print(Fset1)

print("\nEmpty FrozenSet : ")
print(frozenset())
