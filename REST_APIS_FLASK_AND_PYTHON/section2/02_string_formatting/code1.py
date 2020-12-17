name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"
print(greeting)

greeting = f"Hello, {name}"
print(greeting)

print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format("Bob")
with_name_two = greeting.format(name)
print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
