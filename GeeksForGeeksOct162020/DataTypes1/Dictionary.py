Dict = {1: 'Geeks', 2: 'For', 3:'Geeks'}
print("\nDictionary with the use of Integer Keys : ")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys : ")
print(Dict)

Dict = {}
print("Empty Dictionary : ")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict() : ")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair : ")
print(Dict)

Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

Dict = {}
print("Empty Dictionary : ")
print(Dict)

Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements : ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements : ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value : ")
print(Dict)

Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key : ")
print(Dict)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using key : ")
print(Dict['name'])

print("Accessing a element using key : ")
print(Dict[1])

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using get : ")
print(Dict.get(3))
print()

Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])