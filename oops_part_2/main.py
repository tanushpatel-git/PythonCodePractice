# delete the attribute
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Tanu")
print(s1.name)
# del s1.name
print(s1.name)


# inheritence
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

s1 = Student("Tanu", 20, 1)
print(s1.name)
print(s1.age)
print(s1.rollno)

# second example 
class A:
    def __init__(self, name):
        self.name = name

class B(A):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(self.name, "is talking")

    def eat(self):
        print(self.name, "is eating")

class C(B):
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def sleep(self):
        print(self.name, "is sleeping")

s1 = C("Tanu", 20, 1)
s1.talk()
s1.eat()
s1.sleep()
        
# hibride inheritence

class A:
    pass # Something the code is writtten here
class B:
    pass
class C(A,B):
    pass



# property decorder
class Student:
    def __init__(self, name):
        self.name = name

    @property # This thing will help you to call the function like a variable no need of parenthesis and with that it also update the value after the change of value.
    def talk(self):
        print(self.name, "is talking")

    @talk.setter # This thing will help you to update the value of the function.
    def talk(self, name):
        self.name = name

s1 = Student("Tanu")
s1.talk


# classmethod (decorder) -> What if we want to change the name of the class without creating the another instance?
# then we use classmethod
# it also use when we have to change the name into globle level

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def talk(cls):
        print(cls.name, "is talking")

s1 = Student("Tanu", 20)
# s1.talk()


# Polymorphism (Different data types)
# same function name but different different data types 

def talk(a,b):
    print(a + b)

talk(1,2)
talk("Tanu", "Patel")


# public and private access modifier
class Account:
    def __init__(self,acc_no,acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass
        self.__balance = acc_no
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful")

a1 = Account(12345, 1234)
a1.withdraw(1000)


# dunder function
class Dunder_func:
    def __init__(self,num1:int)->int:
        self.num1 = num1

    def __add__(self,other):
        return self.num1 + other.num1
s1 = Dunder_func(10)
s2 = Dunder_func(20)
print(s1 + s2)