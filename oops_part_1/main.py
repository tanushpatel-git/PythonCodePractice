from abc import abstractmethod


class Student:
    name = "Tanu"

st = Student()
print(st.name)
# this is a way to print the memory location of the object


# Constructor
class Student:
    # default constructor
    def __init__(self):
        pass
    # parametrised constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"__init__ method called for object and inside it this is a reference {self}")

st = Student("Tanu",20)
print(st.name)

# for storing the value common for all object we use 
class Student:
    name = "Tanu"

st = Student()
print(st.name)

# Note:
#  When we have the same of attribute and same name of variable we have to use the self keyword to refer the object on that time obj priority is greater then the variable name.


# Taking about Method 
# inside the class u can store data and method 
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name: {self.name} Age: {self.age}")

st = Student("Tanu",20)
st.info()

# getter and setter using method in python thing also come in the encapsulation.
# getter and setter method we are using to get and set the value of the instance variable.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age

st = Student("Tanu",20)
print(st.get_age())
st.set_age(21)
print(st.get_age())


# Static method 
# @staticmethod is a decorator that is used to define a static method in a class.
# static method is a method that is not associated with any instance of the class.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @staticmethod # By using this we are telling that this method is not associated with any instance of the class. basically this not do work in object level or we can say work in a class level. 
    def info():
        print("This is a static method")

st = Student("Tanu",20)
st.info()

# abstraction in oops : This is also a decorator
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side


st = Student("Tanu",20)
st.info()

