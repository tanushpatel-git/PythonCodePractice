# How to make a function in python?
# so lets start
a = 10
b = 10
sum = a + b
print(sum)   # output of this is 20
# but instead to that we can make a function
# we can make a function to do that
def add_to_number(a,b): #def is a keyword to define a function
    sum = a + b
    print(sum)
# and now we able to print the sum value with the help of the function
add_to_number(10,20) # () this is how we call a function

# this is a way to make a type restrict in python
def subtract(a:int,b:int) -> int:
    return a - b

# in this we are telling that the function is taking 2 arguments and returning the value of that arguments 
print(subtract(10,20))


# behind this we can make a recursion using funtion like 
def print_num_up_to_ten(n):
    if n <= 0:
        return
    print(n)
    print_num_up_to_ten(n - 1)
print_num_up_to_ten(10)

# behind this we can make a function using lamda function
square = lambda x: x * x
print(square(10))

# this is a way to make a function using f-string
def greet_person(name):
    return f"Hello, {name}"  # this a type of template literal in python
print(greet_person("Tanush"))
