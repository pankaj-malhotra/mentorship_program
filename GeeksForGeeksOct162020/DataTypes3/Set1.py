Set1 = set()
print("Initial blank set :")
print(Set1)

Set1 = set("GeeksForGeeks")
print("\nSet with the use of string :")
print(Set1)

String = 'GeeksForGeeks'
Set1 = set(String)
print("\nSet with the use of an object :")
print(Set1)

Set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List :")
print(Set1)

Set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of numbers :")
print(Set1)

Set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of mixed values :")
print(Set1)

Set1 = set()
print("\nInitial blank set :")
print(Set1)

Set1.add(8)
Set1.add(9)
Set1.add((6, 7))
print("\nSet after addition of three elements :")
print(Set1)

for i in range(1, 6):
    Set1.add(i)

print("\nSet after addition of elements from 1-5 :")
print(Set1)

Set1 = set([4, 5, (6, 7)])
Set1.update([10, 11])
print("\nSet after addition of elements using update :")
print(Set1)

Set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial Set :")
print(Set1)

print("Elements of Set :")
for i in Set1:
    print(i, end=" ")

print()
print("Geeks" in Set1)

Set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("\nInitial Set :")
print(Set1)

Set1.remove(5)
Set1.remove(6)
print("\nSet after removal of two elements :")
print(Set1)

Set1.discard(8)
Set1.discard(9)
print("\nSet after discarding two elements :")
print(Set1)

for i in range(1, 5):
    Set1.remove(i)

print("\nSet after removing a range of elements :")
print(Set1)

Set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("\nInitial Set :")
print(Set1)

Set1.pop()
print("\nSet after popping an element :")
print(Set1)

Set1 = set([1, 2, 3, 4, 5])
print("\nInitial Set :")
print(Set1)

Set1.clear()
print("\nSet after clearing all the elements :")
print(Set1)

String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
Fset1 = frozenset(String)
print("\nThe FrozenSet is :")
print(Fset1)

print("\nEmpty FrozenSet :")
print(frozenset())


