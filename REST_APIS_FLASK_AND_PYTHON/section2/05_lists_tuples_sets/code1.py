l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

print(l[0])

l[0] ="Smith"
print(l)

l.append("Smith")
print(l)

l.remove("Smith")
print(l)

s.add("Smith")
s.add("Smith")
print(s)
