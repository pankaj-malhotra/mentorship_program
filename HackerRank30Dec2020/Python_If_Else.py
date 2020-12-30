'''
Task
Given an integer,

, perform the following conditional actions:

    If

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than , print Not Weird
'''

print("Enter any number :")
n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif 5 >= n >= 2:
    print("Not Weird")
elif 20 >= n >= 6:
    print("Weird")
elif n > 20:
    print("Not Weird")



