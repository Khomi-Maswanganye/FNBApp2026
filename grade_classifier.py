name = input("Enter your name: ")
grade1 = float(input("Subject 1 mark: "))
grade2 = float(input("Subject 2 mark: "))
grade3 = float(input("Subject 3 mark: "))

ave_grade = (grade1 +grade2 +grade3)/3
gradeletter = ""

gradeStatus = ""

intervention = ""

if ave_grade >= 80:
    gradeletter = "A"
elif ave_grade >= 70:
    gradeletter = "B"
elif ave_grade >= 60:
    gradeletter = "C"
elif ave_grade >= 50:
    gradeletter = "D"
else:
    gradeletter = "F"

if gradeletter == "F":
    gradeStatus = "Fail"
else:
    gradeStatus = "Pass"

if ave_grade <40:
    intervention = "needs intervention"
else:
    intervention = "does not need intervention"

print(f"Name of student: {name}","\n")
print(f"Subject 1 mark: {grade1}","\n")
print(f"Subject 2 mark: {grade2}","\n")
print(f"Subject 3 mark: {grade3}","\n")
print(f"Average grade: {round(ave_grade,2)}","\n")
print(f"Letter grade: {gradeletter}","\n")
print(f"Grade status: {gradeStatus}","\n")
print(f"Intervention needed: {intervention}","\n")
