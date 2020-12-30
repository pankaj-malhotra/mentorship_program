def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print("Total :", multiply(1, 3, 5))


def add(x, y):
    return x + y


nums = [3, 5]
print("Add :", add(*nums))
print("Add :", add(x=3, y=5))

nums = {"x": 15, "y": 25}
print("Add :", add(nums["x"], nums["y"]))
print("Add :", add(x=nums["x"], y=nums["y"]))
print("Add :", add(**nums))


def add1(*args):
    summ = 0
    for arg in args:
        summ = summ + arg
    return summ


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
        #return multiply(args)
    elif operator == "+":
        #return sum(args)
        return add1(*args)
    else:
        return "No valid operator provided by apply()."


print("Apply * :", apply(1, 3, 6, 7, operator="*"))
print("Appy + :", apply(1, 3, 6, 7, operator="+"))





