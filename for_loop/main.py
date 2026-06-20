# Simple first is for loop using range keyword
# The condition for the loop is the we have to print the list of numbers from 1 to 20
for i in range(1,21):
    print(i)


# ---> This same thing we can do with while loop
i = 1
while i < 22:
    print(i)
    i+=1
 
# in range keyword i want to say that range take three peremeter first starting point which is include in the loop and second is ending point which is exclude in the loop and third is updation in a loop
# Here i want to print the even numbers from 1 to 100
for j in range(1,101,2):
    print(j)

# some thing about for each loop
arr = [1,2,3,4,5,5,6]
for a in arr:
    print(a)

# loop in directory is 
schema = {
    "name":"Tanu",
    "roll_no":55,
    "age":19,
    "city":"Bhopal",
    "caste":" OBC"

}

for a,b in schema.items():
    print(a,b)

# one more way is 
for a in schema:
    print(schema[a]) # only print the ans