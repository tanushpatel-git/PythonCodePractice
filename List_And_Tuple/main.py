# --------------------------- List -> Mutable Data type which can we change --------------------------------
marks = [23.5, 63.2, 78.3, 89.2, 87.8]
print(marks)
print(type(marks))
print(len(marks))
print("Marks of 1st postion ->",marks[0])


# ----------------------- Slice in List ------------------------------
print(marks[0:3])
print(marks[-3:-1])


# ------------------------- Method of list --------------------------
marks.append(23.4)
print("Print Marks After append ->", marks)
marks.sort()
print("Print After using short method ->" , marks)
marks.sort(reverse=True)
print("Print After using Shorting in reverse ->" , marks)
marks.reverse()
print("Print Marks after using reverse ->" , marks)
marks.insert(2,12.3)
print("Print marks after insert one float number in list ->", marks)


# -------------------------------- Tupple -> ImMutable Datatype which can't be change -------------------------
mark = (2,1,3,4)
print(type(mark)) # this is a type of tupple 
# this is a  empty tupple
mark1 = ()
# if u want to make a tupple from only single value 
mark2 = (1,)
print(type(mark2), "This is a marks 2 with single value.")
# tupple with multiple value 
mark3 = (1,2,3,4,5,6,7)
print(type(mark3), "This is a tupple with multiple value.")
print(mark3[1:3])
print(mark3.count(2), "How many time 2 come in tupple.")
print(mark3.index(7), "This is a something where u can kown the 7 is when come first time in tupple.")


# -------------------------------- Question 1 for practice using list ------------------------------------
movies = []
first_movie_name = str(input("Enter your first movie name."))
movies.append(first_movie_name)
second_movie_name = str(input("Enter your Second movie name."))
movies.append(second_movie_name)
third_movie_name  = str(input("Enter your third movie name."))
movies.append(third_movie_name)
print("Your total movies is ", movies)

# -------------------------------- Question 2 for practice using list ---------------------------------

list1 = [1,2,3,2,1]
tempList1 = list1.copy()
tempList1.reverse()

if (list1 == tempList1) :
    print("This is a palindrom for list 1 ")
else:
    print("This is not a palindrom for list 1")


# ------------------------------ Question 3 for practice using tupple -----------------------------
grade = ("A", "B", "D" , "F" , "A" , "A")
print(grade.count("A") , "No . of A come in student.")