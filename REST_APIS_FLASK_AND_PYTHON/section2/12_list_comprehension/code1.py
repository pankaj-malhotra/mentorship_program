numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)

doubled = [ x * 2 for x in numbers ]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)
print(friends == starts_s)
print(friends is starts_s)
print(friends[0] == starts_s[0])
print(friends[0] is starts_s[0])

print("friends :", id(friends), "starts_s :", id(starts_s))
print("friends[0] :", id(friends[0]), "starts_s[0] :", id(starts_s[0]))

starts_s = friends
print(friends is starts_s)
