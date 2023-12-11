class Phone:
    def say(self, name):
        self.x = name  # self is used to access the variables inside a class
        print("Hello " + name)



# phone1 = Phone()
# phone1.say("Iroshan")
# print(phone1.x)
# phone1.x = "iPhone"
# print(phone1.x)


# phone2 = Phone()
# phone2.say("Apple")

# -----------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self, name, age):  # automatically called when an object is created
        self.name = name
        self.age = age
        print("Hello! %s you're %i." % (name, age))


# st1 = Student('Iroshan', 25)
# st2 = Student('Shihan', 22)

# -----------------------------------------------------------------------------------------------------------

class Police:
    x = 10  # only x is available for the external
    __y = 20  # this is a private variable, cannot be called seperately

    def disp(self):  # in order to access the private variable
        return self.__y

    # ----------------------------------------------------------------------

    def meth1(self):  # Can be accessed from externally
        print("Hello")
        self.__meth2()  # now we can access the private method

    def __meth2(self):  # Cannot be accessed externally, because this is private, only the class it self can use these
        print("Welcome")


# obj = Police()
# print(obj.x)
# print(obj.disp())
# print(obj.__y) #this is not accessible

# myobj = Police()
# myobj.meth1()
# -----------------------------------------------------------------------------------------------------------

class Car1:  # This is the parent class
    def feature1(self):
        print('body')


class Car2:  # another super class
    def feature2(self):
        print('body_type')


class Car3(Car1):  # Inherit all the attributes and methods from the Car1 class, child class
    def feature3(self):
        print('color')

    def feature1(self):  # method overriding (if this wasn't defined then it would return the value from Car1
        print('body_color')


class Car4(Car3):  # multi-level inheritance this is a sub class of the class Car2
    def feature4(self):  # hence it inherits all methods from Car2 which inherits methods from Car1 class
        print('Wheels')


class Car5(Car4, Car2):  # multiple inheritance
    def feature5(self):
        super().feature1()  # this super function can call other functions inherited from parent classes without
        # having to call them, works like init
        super().feature3()
        print('brand')


# obj1 = Car4()
# obj1.feature1()
# obj2 = Car5()
# obj2.feature2()
# obj2.feature1()  # without the super function
# obj2.feature5()
# -----------------------------------------------------------------------------------------------------------

class Fruit:
    num_items = None
    unit_price = None

    def set_value(self, x, y):
        self.num_items = x
        self.unit_price = y


class Apple(Fruit):
    def price(self):
        _ = self.num_items * self.unit_price
        print('For Apple ', _)
        return _


class Orange(Fruit):
    def price(self):
        _ = self.num_items * self.unit_price
        print('For Orange ', _)
        return _


class Grapes(Fruit):
    def price(self):
        _ = self.num_items * self.unit_price
        print('For Grapes ', _)
        return _


# objF1 = Apple()
# objF2 = Orange()
# objF3 = Grapes()

# objF1.set_value(5,60)
# print(objF1.price())
# x = objF1.price()
# print(type(x))

# objF2.set_value(10,80)
# y = objF2.price()

# objF3.set_value(20,20)
# objF3.price()
# print('Total is,', objF1.price()+objF2.price()+objF3.price())
# -----------------------------------------------------------------------------------------------------------

from test_module import cal
# import test_module => then test_module.cal
# import test_module.cal as cal
import datetime


# i = 25
# j = 5
# print(cal.add(i, j),cal.sub(i, j),cal.mul(i, j),cal.div(i, j))
# b_day = datetime.date(2016,10,16)
# today = datetime.date.today()
# print(today.strftime('%A, %B, %d, %Y'))
# -----------------------------------------------------------------------------------------------------------


def apple(unitprice):
    return lambda number_of: number_of * unitprice


# x = apple(50)
# print(x(10))
# -----------------------------------------------------------------------------------------------------------

# from functools import reduce

number = [1, 2, 3, 4, 5, 6, 7, 8]


def even_num(x):
    return x % 2 == 0


# y = list(filter(even_num, number))
# y = list(filter(lambda x: x%2==0, number))

# a,*y,b = map(lambda x:x*2,number)

# a = reduce(lambda x,y: x*y,number)
# -----------------------------------------------------------------------------------------------------------

def new(func):  # decorator
    def inside(a, b):
        if b == 0:
            a, b = b, a
        return func(a, b)

    return inside


@new  # good practice
def divide(a, b):
    return a / b


# divide = new(divide)  # not good practice
# print(divide(5, 0))
# -----------------------------------------------------------------------------------------------------------

class Parent:
    age = 40

    def greet(self):
        print('Hello')


class Child(Parent):
    age = 15

    def greet(self):
        print('Hi')
        return "I'm Iroshan"


# obj = Child()
# obj.greet()
# print(obj.greet())
# -----------------------------------------------------------------------------------------------------------

class Calc:
    def add(self, a, *b):
        sum = a
        for _ in b:
            sum += _
        print(sum)


myObj = Calc()
myObj.add(2)
myObj.add(2, 5)
myObj.add(2, 5, 10)
myObj.add(2, 5, 10, 100)
myObj.add(2, 5, 10, 100, 1000)


# -----------------------------------------------------------------------------------------------------------


class Itr1:
    def __init__(self):
        self.y = 2

    def __iter__(self):
        return self

    def __next__(self):  # there is an error
        val = self.y
        self.y += 2
        return val


myObj = Itr1()
itr = iter(myObj)
print(next(itr))
print(next(itr))
print(next(itr))


# -----------------------------------------------------------------------------------------------------------


def fib():  # generators
    a, b = 0, 1
    while True:
        c = a + b
        yield a
        a, b = b, c
# -----------------------------------------------------------------------------------------------------------


from threading import *


def fun1():
    for _ in range(100):
        print('Iroshan')


def fun2():
    for _ in range(100):
        print('Shihan')


def fun3():
    for _ in range(100):
        print('Rajitha')


def fun4():
    for _ in range(100):
        print('Dhanushi')


t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
# t3 = threading.Thread(target=fun3)
# t4 = threading.Thread(target=fun4)

t1.start()
t2.start()
# t3.start()
# t4.start()
# -----------------------------------------------------------------------------------------------------------


class A(Thread):
    def run(self):
        for _ in range(10):
            print('Hello')

class B(Thread):
    def run(self):
        for _ in range(10):
            print('Hi')

obj1 = A()
obj2 = B()
obj1.start()  # this executes a method call run in the class
obj2.start()
obj1.join()  # this executes a method call run in the class
obj2.join()
print('Bye', current_thread().getName())
# -----------------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg < 40:
            return "T"
        elif avg < 55:
            return "D"
        elif avg < 70:
            return "P"
        elif avg < 80:
            return "A"
        elif avg < 90:
            return "E"
        else:
            return "O"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


# -----------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
            self.tail = head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head
    # Complete this method


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)

# -----------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------
