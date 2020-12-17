class Test:
    def fun(self):
        print("Hello")


obj = Test()
obj.fun()
print('-' * 10)


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ', self.name)


p = Person('Shwetanshu')
p.say_hi()
print('-' * 10)


class CSStudent:
    stream = 'cse'

    def __init__(self, roll):
        self.roll = roll


a = CSStudent(101)
b = CSStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)
print(CSStudent.stream)
print('-' * 10)


class CSStudent1:
    stream = 'cse'

    def __init__(self,roll):
        self.roll = roll

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address


a = CSStudent1(101)
a.setAddress("Noida, UP")
print(a.getAddress())
print('-' * 10)


class Test1:
    pass

