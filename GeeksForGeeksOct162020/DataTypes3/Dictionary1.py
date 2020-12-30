Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys :")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys :")
print(Dict)

Dict = {}
print("\nEmpty Dictionary :")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with each item as a pair :")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair :")
print(Dict)

Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

Dict = {}
print("\nEmpty Dictionary :")
print(Dict)

Dict[0] = 'Geeks'
Dict[1] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements :")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after 3 elements :")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value :")
print(Dict)

Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key :")
print(Dict)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\nAccessing an element using key :")
print(Dict['name'])
print("Accessing an element using key :")
print(Dict[1])

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\nAccessing an element using get :")
print(Dict.get(3))

print()

Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

print("\nAnother way using get method :")
print(Dict.get('Dict1'))
print(Dict.get('Dict1').get(1))
print(Dict.get('Dict2').get('Name'))

Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("\nInitial Dictionary :")
print(Dict)

del Dict[6]
print("\nDeleting a specific key :")
print(Dict)

del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary :")
print(Dict)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.pop(1)
print("\nDictionary after deletion :", Dict)
print("Value associated to poped key is :", pop_ele)

print("\nDictionary after deletion :" + str(Dict))
print("Value associated to poped key is :" + pop_ele)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.popitem()
print("\nDictionary after deletion :", Dict)
print("The arbitrary pair returned is :", pop_ele)

print("\nDictionary after deletion :" + str(Dict))
print("The arbitrary pair returned is :" + str(pop_ele))

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
Dict.clear()
print("\nDeleting entire dictionary :")
print(Dict)

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary Keys :")
print(Dict.keys())

print("Dictionary values :")
print(Dict.values())

print("Dictionary items :")
print(Dict.items())








