#initialize
gross_income=0
sss_contri=0
philhealth_contri=0
total_deduction=0
net_income=0
pagibig_contri=100.00
emp_name=""
emp_depart=""

#input
emp_name= str(input("Employee's Name:"))
emp_depart= str(input("Department:"))
rate_per_hr= float(input("Employee's Rate per Hour:"))
hrs_per_day= float(input("Employee's Hours per Day:"))
days_per_week= float(input("Employee's Days per Week:"))
weeks_per_month= float(input("Emloyee's Weeks per Month:"))

#calculations gross income
gross_income= rate_per_hr*hrs_per_day*days_per_week*weeks_per_month


#ssscontribution
if 0 <= gross_income <= 20000:
        sss_contri= 125.75
elif 20001 <= gross_income <= 50000:
        sss_contri= 2200.50
elif 50001 <= gross_income <= 75000:
        sss_contri= 4800.00
elif gross_income > 75000:
        sss_contri= 5800.00

total_deduction = sss_contri + philhealth_contri + pagibig_contri

#philhealth_contri
if 0 <= gross_income <= 20000:
        philhealth_contri= 100.00
elif 20001 <= gross_income <= 50000:
        philhealth_contri= 1200.00
elif 50001 <= gross_income <= 75000:
        philhealth_contri= 6800.00
elif gross_income > 75000:
        philhealth_contri= 8800.00

total_deduction = sss_contri + philhealth_contri + pagibig_contri

#net income
net_income= gross_income-total_deduction

#display
print("Employee Name:", emp_name)
print("Department:", emp_depart)
print("Gross Income:", gross_income)
print("Total Deduction:", total_deduction)
print("Net Income:", net_income)