def myFunction():
    print("myFunction")

myFunction()

def myFunctionWith(param):
    print(param)

myFunctionWith("Codekul")

def myFunctionWithDefault(param = "Codekul"):
    print(param)

myFunctionWithDefault("MeLayer")

def functionWithReturningValue():
    return "Codekul"

print(functionWithReturningValue())

def changeTheValue(data):
    data = 100

data = 10
changeTheValue(data)
print(data)

def changeTheList(list):
    # list.append(100)
    list = [6,7,8,9,0]

list = [1,2,3,4,5]
changeTheList(list)
print(list)

def calculateTheAreaOfCircle(rad):
    return 3.14*(rad**2)

area = calculateTheAreaOfCircle(33)

print("Area of circle: {}".format(area))


def function1(data):
    print(data)

def function2(function, data):
    function(data)

function2(function1, 20)


def recursive(data):
    data -= 1
    if data == 0:
        return
    recursive(data)
    print(data)

recursive(5)

