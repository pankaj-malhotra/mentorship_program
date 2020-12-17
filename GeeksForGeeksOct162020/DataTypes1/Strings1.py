String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes : ")
print(String1)

String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String : ")
print(String1)
print()

String1 = "GeeksForGeeks"
print("Initial String : ")
print(String1)

print("\nFirst character of String is : ")
print(String1[0])

print("\nLast character of String is : ")
print(String1[-1])

print("\nSlicing characters from 3-12 : ")
print(String1[3:12])

print("\nSlicing characters between 3rd and 2nd last character : ")
print(String1[3:-2])
print()

String1 = "Hello, I'm a Geek"
print("Initial String : ")
print(String1)

"""
String1[2] = 'p'
print("\nUpdating character at 2nd Index : ")
print(String1)
"""

String1 = "Welcome to the Geek World"
print("\nUpdated String : ")
print(String1)

String1 = "Hello, I'm a Geek"
print("Initial String : ")
print(String1)
print()

"""
del String1[2]
print("\nDeleting character at 2nd Index : ")
print(String1)


del String1
print("\nDeleting entire String : ")
print(String1)
"""

String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes : ")
print(String1)

String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote : ")
print(String1)

String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes : ")
print(String1)

String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes : ")
print(String1)

String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences : ")
print(String1)

String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format : ")
print(String1)
print()

String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order : ")
print(String1)

String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order : ")
print(String1)

String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of keywords : ")
print(String1)
print()

String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is : ")
print(String1)

String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is : ")
print(String1)

String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)
print()

String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
print("\nLeft, center and right alignment with Formatting : ")
print(String1)

String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)
print()

Integer1 = 12.3456789
print("Formatting in 3.2f format : ")
print('The value of Integer1 is %3.2f' %Integer1)
print("\nFormatting in 3.4f format : ")
print('The value of Integer1 is %3.4f' %Integer1)

