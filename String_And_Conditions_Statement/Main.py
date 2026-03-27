# Declaration of string in different way.

str1 = "this is a str 1"
str2 = 'this is a str 2'
str3 = """this is a str 3"""


# --------------------------------------------Q1. Why the thing is need to use that three way and which is most of the time prefer.--------------------------------------
# Ans. Suppose the thing is if u wanna written --------> 'this is Tanush's mother' so we can't write it in that way we have to use " " in out  side os this type sentence.



# ----------------------------------------Use of scape sequence char in.----------------------------------------

print("=====================After giving space sequence.===================================")
print("Tanush - What's a whether today. Rahul- It's something around 32 deg celsius") # this thing print in straight line.
print("Tanush - What's a whether today. \nRahul- It's something around 32 deg celsius") # this \n give next line access.
print("=====================After giving Tab space.===================================")
print("Tanush - \t What's a whether today. \nRahul - \t It's something around 32 deg celsius") #this \t give tab like space in sentence.

# 1. ----------------------------------------- Concatenation -----------------------------------------

str4 = "My name is "
str5 = "Tanush"
print(str4 + str5)

# 2. ----------------------------------------- Find length of string -----------------------------------------

print("Length of the string (no. of letter in sentence or word including space also) is -> ",len(str4 + str5))


# 3. ----------------------------------------- Index of String is -----------------------------------------

print("third index of string is " , str4[3]) # Ans is n

# ----------------------------------------- Slice in String is -----------------------------------------

# str3[2:3]
# str3[3:]

print("Slice of string in whole Sentence is", str5[:4]) # it means [ 0 to 3 letter include ].

# Restrict thing in slice or separation thing is

# str4[2] = "R"
# print(str4)

# You can see the slice in negative index also

newStr = "TanushProCoder" # this thing work in reverse side of the string like the TanushProCoder is look like --> -14 , -13 ,-12 to 0 the index is follow like this
print(newStr[-14:])

# ----------------------------------------- String Function is ---------------------------------------------------

prac_str = "I Live in Bhopal"
print(prac_str.count("i") + prac_str.count("I")) # Number of time occurrence is
print(prac_str.find("L")) # returns 1st index of 1st occurrence
tempString = prac_str.replace("B", "K") # replaces all occurrences of old with new
print("After Replace B by K", tempString)
print("Capitalize first letter using fucn", ("tanush").capitalize()) #capitalizes 1st char
print("This is a line turn all word upper case",("Tanush").upper())
print("Is Hello is end with lle", ("Hello").endswith("llo")) #returns true if string ends with substr



# --------------------------------------                         ----------------------------------------
# --------------------------------------  Conditional Statement  ---------------------------------------
# --------------------------------------                         ----------------------------------------


age = int(input("Enter Your Age"))

if(age >= 18):
    print("Adult")
else:
    print("Not Adult")


# -------------------------------- if elif ladder -----------------------------------


light = "Green"

if(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Look")
else:
    print("Wait")


# <---------------------------------- Second Day course Complete ------------------------------------>