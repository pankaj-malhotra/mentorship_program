List = []
print("Blank List :")
print(List)

List = [10, 20, 14]
print("\nList of numbers :")
print(List)

List = ["Geeks", "For", "Geeks"]
print("\nList Items :")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List :")
print(List)

List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of numbers :")
print(List)

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed values :")
print(List)

List1 = []
print("List size :", len(List1))

List2 = [10, 20, 14]
print("List size :", len(List2))

List = []
print("\nInitial blank list :")
print(List)

List.append(1)
List.append(2)
List.append(4)
print("\nList after addition of 3 elements :")
print(List)

for i in range(1, 4):
    List.append(i)
print("\nList after addition of elements from 1-3 :")
print(List)

List.append((5, 6))
print("\nList after addition of a Tuple :")
print(List)

List2 = ['For', 'Geeks']
List.append(List2)
print("\nLIst after addition of a List :")
print(List)

List = [1, 2, 3, 4]
print("\nInitial List :")
print(List)

List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert operations :")
print(List)

List = [1, 2, 3, 4]
print("\nInitial List :")
print(List)

List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend operation :")
print(List)

List = ["Geeks", "For", 'Geeks']
print("\nAccessing an element from the list :")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("Accessing an element from a Multi-Dimensional list :")
print(List[0][1])
print(List[1][0])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nAccessing element using negative indexing :")
print(List[-1])
print(List[-3])

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("\nInitial List :")
print(List)

List.remove(5)
List.remove(6)
print("List after removal of two elements :")
print(List)

for i in range(1, 5):
    List.remove(i)

print("List after removing a range of elements :")
print(List)

List = [1, 2, 3, 4, 5]
List.pop()
print("\nList after popping an element :")
print(List)

List.pop(2)
print("List after popping a specific element :")
print(List)

List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("\nInitial List :")
print(List)

Sliced_List = List[3:8]
print("Slicing elements in a range 3-8 :")
print(Sliced_List)

Sliced_List = List[5:]
print("Elements sliced from 5th element till the end :")
print(Sliced_List)

Sliced_List = List[:]
print("Printing all elements using slice operation :")
print(Sliced_List)

Sliced_List = List[:-6]
print("Elements sliced till 6th element from last :")
print(Sliced_List)

Sliced_List = List[-6:-1]
print("Elements sliced from index -6 to -1 :")
print(Sliced_List)

Sliced_List = List[::-1]
print("Printing List in reverse :")
print(Sliced_List)


