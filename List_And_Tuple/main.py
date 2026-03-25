# --------------------------- List --------------------------------
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