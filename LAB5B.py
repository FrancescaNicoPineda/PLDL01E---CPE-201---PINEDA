import LAB5A
obj = LAB5A.StudentInfo()
student_name = input("Enter Student Name: ")
course = input("Enter Course: ")
student_number = input("Enter Student Number: ")
acad_year = input("Enter Academic Year: ")
current_date = input("Enter Current Date (MM/DD/YYYY): ")
downpayment = float(input("Enter Downpayment: "))
student_data = obj.get_student_info(student_name, course, student_number, acad_year, current_date, downpayment)

obj2 = LAB5A.UnitInfo()
unit_info = LAB5A.UnitInfo()
num_subjects = int(input("Enter number of subjects: "))
for i in range(num_subjects):
    section = input(f"Enter Section for Subject {i+1}: ")
    subject = input(f"Enter Subject {i+1}: ")
    units = int(input(f"Enter Units for Subject {i+1}: "))
    unit_info.add_subject(section, subject, units)

# Create an instance of FeeComputation and set its parameters
assessment = LAB5A.Assessment()
fee_computation = LAB5A.FeeComputation(assessment, student_data["downpayment"])

# Compute total due and payment schedule
total_due = fee_computation.get_total_due()
payment_schedule = fee_computation.get_payment_schedule()

print("\n=================== Student Information ===================")
student.display_student_data()
print("\n=================== Enrolled Units ===================")
unit_info.display_units()
print("\n=================== Assessment Details ===================")
print("Tuition Fee Lecture: P", f"{assessment.tuition_fee:,.2f}")
print("Assessment Amount: P", f"{assessment.get_total_assessment():,.2f}")
print("Downpayment: P", f"{downpayment:,.2f}")
print("Total Due: P", f"{total_due:,.2f}")
print("\n=================== Payment Schedule ===================")
print("Prelims: P", f"{payment_schedule:,.2f}")
print("Midterms: P", f"{payment_schedule:,.2f}")
print("Finals: P", f"{payment_schedule:,.2f}")
