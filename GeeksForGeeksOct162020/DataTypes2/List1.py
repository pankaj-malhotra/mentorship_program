List = []

print("Blank List:")
print(List)

List = [10, 20, 14]
print("\nList of numbers:")
print(List)

List = ["Geeks", "For", "Geeks"]
print(List)
print("\nList Items:")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List:")
print(List)

List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers:")
print(List)

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values:")
print(List)

List1 = []
print(len(List1))

List2 = [10, 20, 14]
print(len(List2))

List = []
print("Initial blank List:")
print(List)

List.append(1)
List.append(2)
List.append(4)

print("\nList after addition of three elements:")
print(List)

for i in range(1, 4):
    List.append(i)

print("\nList after addition of elements from 1-3:")
print(List)

List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after addition of a List:")
print(List)
print()

for i in range(0, len(List)):
    print(List[i])

List = [1, 2, 3, 4]
print("Initial List :")
print(List)

List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing insert operation:")
print(List)

List = [1, 2, 3, 4]
print("Initial List:")
print(List)

List.extend([8, 'Geeks', 'Always'])
print("\nList after performing extend operation:")
print(List)


List = ["Geeks", "For", "Geeks"]
print("Accessing an element from the list:")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]

print("Accessing an element from a Multi-dimensional list:")
print(List[0][1])
print(List[1][0])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

print("Accessing element using negative indexing:")
print(List[-1])
print(List[-3])


List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Initial List:")
print(List)

List.remove(5)
List.remove(6)
print("\nList after removal of two elements:")
print(List)

for i in range(1, 5):
    List.remove(i)

print("\nList after removing a range of elements:")
print(List)

List = ['Geeks', 'Raj', 'For', 'Geeks', 8, 'Geeks', 'Always']

print("\nInitial List:")
List.remove("Geeks")

print("\nList after removal:", List)

List = [1, 2, 3, 4, 5]

List.pop()
print("\nList after popping an element:")
print(List)

List.pop(2)
print("\nList after popping a specific element:")
print(List)


List = ['G', 'E', 'E', 'K', 'S', 'F',
        'O', 'R', 'G', 'E', 'E', 'K', 'S']

print("Initial List:")
print(List)

Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8:")
print(Sliced_List)

Sliced_List = List[:]
print("\nPrinting all elements using slice operation:")
print(Sliced_List)

Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last:")
print(Sliced_List)

Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1 :")
print(Sliced_List)

Sliced_List = List[::-1]
print("\nPrinting List in reverse :")
print(Sliced_List)

Sliced_List.sort()
print("\nSorted List:", Sliced_List)

Sliced_List.reverse()
print("\nReversed sorted list:", Sliced_List)

Sliced_List.clear()
print(Sliced_List)

List1 = ["Geeks", "For", "Geeks"]
List1.insert(1, "Raj")

List1.extend([8, "Geeks", "Always"])

print(List1)

for i in List1:
    print(i, end= " ")




