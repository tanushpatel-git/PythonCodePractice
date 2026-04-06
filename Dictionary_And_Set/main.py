# -------------------------------- Dictionary  --------------------------------------


info_About_Tanush = { # ---->  key should'nt be list 
    "Name" : "Tanush",
    "Age" : 19,
    "Mob no." : 9729346173,
    "Gender" : "Male",
    "is_Adult" : True,
    "Hard_Skill" : ["React", "Express", "Gin", "Tailwind" , "GenAi"],
    "Languages" : ("Java" , "Python" , "GoLang", "Javascript")
}
# Dictionary are mutable like a list
# ---> in Dictionary key should'nt be repeated 

print(type(info_About_Tanush))  # type of dictionary is class <"dict">

# info from dictionary 
print(info_About_Tanush["Name"]) # Tanush
print(info_About_Tanush["Age"]) # 19
# print(info_About_Tanush["noExisted"]) # Throw a error like this thing is not existed


# if u want to add new detail after dictionary 
info_About_Tanush["surname"] = "Patel"

print("This is a new disctionary ->" , info_About_Tanush)

# if we want we can create a  empty dictionary 

emptyDictionary = {}

print("emptyDictionary -> ", emptyDictionary)

# -------------------------------- Nested Dictionary ---------------------------------

schoolData = {
    "Name" : "Tanush",
    "Score" : {
        "Math" : 96,
        "Phy" : 89,
        "Chem"  :78,
        "Eng" : 98,
        "Hin" : 73
    },
    "Subject":("Math", "English" , "Chemistry", "Physics", "Hindi")
}


# ---------------------------- Methods of dictionary -----------------------------------

pairs = list(schoolData.values())
print(list(schoolData.keys())) # doing type cast for taking key of dic
print("Value of School data 1 -> ", pairs[0])
print("Value of School data 2 -> ", pairs[1])
print("Value of School data 3 -> ", pairs[2])
# if we want to get the whole key and val in the form of tupple for that u have to do for example -> ("key" , "val")
print("School data in tupple form is ->", list(schoolData.items()))

# ---------------------------- Get the value by get method ----------------------------
print(list(schoolData.get("Score")))


# ---------------------------- if u want to update new key value pair ----------------------------
new_dict = {"city" : "Bhopal" , "Age" : 20 , "Name" : "Tanu"}
schoolData.update(new_dict)
print("After the updation school data is " , schoolData) # bsically it override the old value and change with new value





# ---------------------------- Set in Python ----------------------------
 
collection = {1,2,4,4,5,6,"Tanu", "Patel"} # Set Can't store duplicate value and set in mutable but set element are immutable so it not store list and dict in inside that beacause they change their value.
print(type(collection)) # class <set>
print(collection) # 1,2,5,4,6,"Tanu","Patel"

# if u want to create a empty set u can write like 
emptyCollection = set()

# ---------------------------- Method use in set ----------------------------
collection.add("Tanush")
collection.remove("Tanush")
collection.add((1,2,4,5))
# collection.remove("notExistedValue") # Throw and error by python that value is not existed
print(collection.pop()) # it just give as a random value from set
collection.clear()


# Union in set 

set1 = {1,2,3}
set2 = {2,3,4}

# --> Give the unique value and remove duplicate form set 1 and set 2
print("Union of set 1 and set 2 ->",set1.union(set2)) # output is {1,2,3,4}

# Intersection of set1 and set2 
# ---> Give the common value of set 1 and set 2 
print("Intersection of set 1 and set 2 ->",set1.intersection(set2)) # output is {2,3}