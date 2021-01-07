'''
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example
n = 3
The list of non-negative integers that are less than is . Print the square of each number on a separate line.

Print
0
1
4

'''

print("Enter any number :")
n = int(input().strip())

for i in range(0, n):
    print(i * i)


