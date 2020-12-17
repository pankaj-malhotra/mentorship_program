def hello():
    print("Hello!")

hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age :"))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")

#def print():
#    print("Hello, world!")

friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name :")
    #friends = friends + friend_name
    #f = friends + friend_name
    friends.append(friend_name)

add_friend()
print(friends)
print()


def add_friend():
    fri.append("Rolf")

fri = []
add_friend()
add_friend()
add_friend()

print(fri)
