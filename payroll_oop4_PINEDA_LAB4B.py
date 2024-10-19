#this program will simple access the codes under payroll_oop2.py
# #this progam will compute the partial deduction of an employee

import payroll_oop2_PINEDA_LAB4B

#Instantiate payroll_oop2.py and place it inside the employee payroll. Note: Employee payroll is changeable as you wish
employee_payroll = payroll_oop2_PINEDA_LAB4B.Employee_Salary()
emp_rate_per_hour = float(input("Enter value for rate per our: "))
emp_num_of_absences = int(input("Enter value for number of absences: "))
tardiness_hours = int(input("Enter number of tardiness: "))

#Accessing the codes under the attribute get absences deduction inside the Employee Salary class.
absences_deduction = employee_payroll.get_absences_deduction(emp_rate_per_hour, emp_num_of_absences)
tardiness_deduction = employee_payroll.get_tardiness_deduction(emp_rate_per_hour, tardiness_hours)

#Formula to compute the partial deduction of an employee
partial_deduction = absences_deduction + tardiness_deduction
print("Employee partial deduction is: %.2f" % partial_deduction)