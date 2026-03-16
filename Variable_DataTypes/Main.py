# Hello World in python is

print("Hello World in python is") # it is a code in python to print the word inside a ""


# Data type is --->
# 1. Integer,
# 2. String,
# 3. Boolean,
# 4. Float,
# 5. None


age = 20
name = "Tanush"
isAdult = True
amount = 30.3
val_check_none = None

print(age)
print(name)
print(isAdult)
print(amount)
print(val_check_none)


# ------------------------------Arithmetic operator is ---------------------------------------

num1 = 3
num2 = 3
print("num1", num1)
print("num2", num2)
mul_num = num1 * num2 # multiply
# num2*=num1 # Advance method or a Assignment operator
print("Mul is", mul_num)
add_num = num1 + num2 # addition
# num2 += num1 # Advance method or a Assignment operator
print("Add is", add_num)
sub_num = num1 - num2 # subtraction
# num2-=num1 # Advance method or a Assignment operator
print("Sub is", sub_num)
pow_num = num1 ** num2 # num1 ^ nums2
# num1**=num2 # Advance method or a Assignment operator
print("Pow is", pow_num)
div_num = num1 / num2 # divide (it give value in float)
# num2/=num1 # Advance method or a Assignment operator
print("Div is", div_num)


# ------------------------------comparison operator is ----------------------------------------------

print("num1 > num2", num1 > num2)
print("num1 < num2", num1 < num2)
print("num1 >= num2", num1 >= num2)
print("num1 <= num2", num1 <= num2)
print("num1 == num2", num1 == num2)
print("num1 != num2", num1 != num2)


# -------------------------------Logical Operator is -------------------------------------------------

# not operator is
a = 30
b = 50
temp = True
print("A is greater than B Answer is False but we show output true using not operator", not (a > b))
print("Opposite of temp using not operator", not (temp))
# and operator is (&)
print("Find the ans using operator or", (not (a > b)) or (not (a < b))) # u can use it as a |
print("Find the ans using operator and", (not (a > b)) and (not (a < b))) # u can use it as a &


# -------------------------------type conversion in python is -------------------------------------------

num3 = 2
num4 = 3.2
print(num3 + num4) # Auto type cast python it for us in higher version in this case float is a superior version
# ---------Manually type case example is--------- #
num5 = "2"
num6 = 3
print(int(num5) + num6) # In this case string is not allow by python to add with integer and python not do auto type cast it also so we do a force or we can say a manual type cast
print(num5 + str(num6)) # we can do conver it manually


# Q1. imp basic question is
# temp2 = "Buddha"
# print(int(temp2))


# Input in python in three ways

name2 = input("Enter your Name here :")
print("Hello", name2)
num7 = input("Enter your Number Here :")
print("Value of num7 is", num7)
 # int(input("Enter any number here")) # type cast using in input


#Pratice question


# Q2. ------------------------------- take a input of two number and print their sum --------------------------------
print("Find the sum of two number")
first = int(input("Enter your first Number Here :"))
second = int(input("Enter your second Number Here :"))
print("Sum of num is ", first + second)


# Q3. --------------------------------- take a side of the square and print the area of the square --------------------------
print("For Area of square")
sideLen = int(input("Enter your side Length in meter Here :"))
print("Area of side is", sideLen**2 , "m^2")


# Q4. --------------------------------- Take a two num and print the average number of both num -------------------------------
print("For finding the Average of two number ")
firstNum = float(input("Enter your first Number Here :"))
secondNum = float(input("Enter your second Number Here :"))
print("Average of two number is " , (firstNum + secondNum)/2)

# Q5. ---------------------------------WAP to input two number a and b and print true if a is greater than b otherwise false
print("Bool of a is greater than and equal to b")
val_a = int(input("Enter your Value Here :"))
val_b = int(input("Enter your Value Here :"))
print("A is greater than B" , (val_a >= val_b))





# <---------------------------------- First Day course Complete ------------------------------------>