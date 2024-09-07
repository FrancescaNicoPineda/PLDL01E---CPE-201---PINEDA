#initialize
final_grade=0
student_name=""
equivalent_grade=0

#input
student_name= str(input("Student Name:"))
final_quizzes= float(input("Final Quiz Rating:"))
final_assignment= float(input("Final Assignment/Research Rating:"))
final_project= float(input("Final Project Rating:"))
final_exam= float(input("Final Exam Rating:"))

#computation
final_grade = (0.30 * final_quizzes) + (0.10 * final_assignment) + (0.40 * final_exam) + (0.20 * final_project)

#grade scaling
if 98 <= final_grade <= 100:
        equivalent_grade =4.00
elif 95 <= final_grade < 98:
        equivalent_grade =3.75
elif 92 <= final_grade <= 94:
        equivalent_grade =3.50
elif 89 <= final_grade <= 91:
        equivalent_grade =3.25
elif 86 <= final_grade <= 88:
        equivalent_grade =3.00
elif 83 <= final_grade <= 85:
        equivalent_grade =2.75
elif 80 <= final_grade <= 82:
        equivalent_grade =2.50
elif 77 <= final_grade <= 79:
        equivalent_grade =2.25
elif 74 <= final_grade <= 76:
        equivalent_grade =2.00
elif 71 <= final_grade <= 73:
        equivalent_grade =1.75
elif 68 <= final_grade <= 70:
        equivalent_grade =1.50
elif 64 <= final_grade <= 67:
        equivalent_grade =1.25
elif 60 <= final_grade <= 63:
        equivalent_grade =1.00
elif 60 > final_grade:
        equivalent_grade= 0.00


#print
print ("Final Quiz Rating:", final_quizzes)
print ("Final Assignment/Research Rating:", final_assignment)
print ("Final Project Rating:", final_project)
print ("Final Exam Rating:", final_exam)
print ("Final Grade:", round(final_grade, 2))
print ("Equivalent Grade:", equivalent_grade)