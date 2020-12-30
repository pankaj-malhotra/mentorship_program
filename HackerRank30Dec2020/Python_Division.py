'''
The provided code stub reads two integers, and

, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,
// . The second line should contain the result of float division, /

.

No rounding or formatting is necessary.

Example
a = 3
b = 5

Print:
0
0.6

'''


print("Enter first integer :")
a = int(input().strip())

print("Enter second integer :")
b = int(input().strip())

print(int(a / b))
print(float(a / b))
