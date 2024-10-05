#this program will simplify compute the basic pay, hononarium pay, and absences deduction
import payroll_oop2_PINEDA_LAB4B

obj = payroll_oop2_PINEDA_LAB4B.Employee_Info()
company = input("Enter Company Name: ")
department = input("Enter Employee Department: ")
employee_name = input("Enter Employee Name: ")
employee_code = input("Enter Employee Number or Code: ")
salary1_cut_off = str(input("Enter Salary Cut-Off: "))
emp_data = obj.get_emp_data(company, department, employee_name, employee_code, salary1_cut_off)

#data entry for basic pay computation
obj2 = payroll_oop2_PINEDA_LAB4B.Employee_Salary()
rate_pay = float(input("Enter employee rate per hour: "))
number_working_hours = float(input("Enter employee number of working hours: "))
honorarium_pay = float(input("Enter honorarium pay: "))
number_absences = float(input("Enter number of absences in hours: "))

# computation for basic pay
basic_pay = obj2.get_basic_pay(rate_pay, number_working_hours)
absences_deduction = obj2.get_absences_deduction(rate_pay, number_absences)

# display of output
print("________________________________________________________________________")
print("________________________________________________________________________")
obj.desiplay_data()
print("Basic Pay: %.2f" % basic_pay)
print("Honararium Pay: %.2f" % honorarium_pay)
print("Employee absences deduction: %.2f" % absences_deduction)
print("________________________________________________________________________")
print("________________________________________________________________________")

