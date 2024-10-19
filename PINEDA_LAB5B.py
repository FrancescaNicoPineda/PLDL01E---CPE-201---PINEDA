import PINEDA_LAB5A

obj = PINEDA_LAB5A.studentinfo()
student_name = input("Student Name:")
course = input("Course: ")
student_number = input("Student Number: ")
acad_year = input("Academic Year: ")
current_date = input("Current Date: ")
downpayment = float(input("Downpayment: "))
student_info = obj.get_student_info(student_name, course, student_number, acad_year, current_date, downpayment)