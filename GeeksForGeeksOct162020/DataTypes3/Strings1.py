a = "This is a string"
print("a :", a)

L = [1, "a", "string", 1+2]
print("L :", L)
L.append(6)
print("L :", L)
L.pop()
print("L :", L)
print("L[1] :", L[1])

tup = (1, "a", "string", 1+2)
print("tup :", tup)
print("tup[1] :", tup[1])

i = 1
while i < 10:
    print(i, end=" ")
    i = i+1

print()

s = "Hello World"
for i in s:
    print(i, end=" ")

print()

L = [1, 4, 5, 7, 8, 9]
for i in L:
    print(i, end=" ")

print()

for i in range(0, 10):
    print(i, end=" ")
