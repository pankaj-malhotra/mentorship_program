List = []
print("Blank List : ")
print(List)

List = [10, 20, 14]
print("\nList of numbers : ")
print(List)

List = ["Geeks", "For", "Geeks"]
print("\nList Items : ")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List : ")
print(List)
print()

List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers : ")
print(List)

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values : ")
print(List)
print()

List1 = []
print(len(List1))

List2 = [10, 20, 14]
print(len(List2))
print()

List = []
print("Initial blank List : ")
print(List)

List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements : ")
print(List)

for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3 : ")
print(List)

List.append((5, 6))
print("\nList after Addition of a Tuple : ")
print(List)

List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List : ")
print(List)
print()

List = [1, 2, 3, 4]
print("Initial List : ")
print(List)

List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation : ")
print(List)
print()

List = [1, 2, 3, 4]
print("Initial List : ")
print(List)

List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation : ")
print(List)
print()

List = ["Geeks", "For", "Geeks"]
print("Accessing a element from the list : ")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
print("Accessing a element from a Multi-Dimensional list : ")
print(List[0][1])
print(List[1][0])
print()

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("Accessing element using indexing : ")
print(List[-1])
print(List[-3])
print()

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial List : ")
print(List)

List.remove(5)
List.remove(6)
print("\nList after Removal of two elements : ")
print(List)

for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements : ")
print(List)
print()

List = [1, 2, 3, 4, 5]
List.pop()
print("\nList after popping an element : ")
print(List)

List.pop(2)
print("\nList after popping a specific element : ")
print(List)
print()

List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List : ")
print(List)

Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8 : ")
print(Sliced_List)

Sliced_List = List[5:]
print("\nElements sliced from 5th element till the end : ")
print(Sliced_List)

Sliced_List = List[:]
print("\nPrinting all elements using slice operation : ")
print(Sliced_List)
print()

List = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List : ")
print(List)

Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last : ")
print(Sliced_List)

Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1 : ")
print(Sliced_List)

Sliced_List = List[::-1]
print("\nPrinting List in reverse : ")
print(Sliced_List)



