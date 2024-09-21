#initializing inputs
company_name=""
department=""
emp_code=""
emp_name=""
cut_off=0
pay_period=0
pagibig_contri=100
sss_contri= 0
philhealth_contri= 0
rate_hr= 0
hrs_day=0
tardiness=0
absences=0
hononarium=0
OT_hrs=0
OT_pay=0
basic_pay=0
total_deduction=0
gross_income=0
net_income=0
hrs_tardy=0
absences_hrs=0
hononarium_hrs=0
withholding_tax=0
#inputs
company_name=str(input("Company Name:"))
emp_name= str(input("Employee's Name:"))
department= str(input("Department:"))
emp_code= str(input("Employee Code:"))
#Basic Pay of employee
rate_hr= float(input("Employee's Rate per Hour:"))
hrs_day= float(input("Employee's Hours per Day:"))
hrs_tardy= float(input("No. of Hours Tardy:"))
OT_hrs= float(input("No. of Overtime Hours:"))
absences_hrs= float(input("No. of Hours Absent:"))
hononarium_hrs= float(input("No. of Hononarium Hours:"))
cut_off= float(input("Cut-Off:"))
pay_period= float(input("Pay Period:"))
#Pay Calculations
basic_pay=rate_hr*hrs_day
OT_pay=hrs_day*rate_hr
hononarium= hononarium_hrs*rate_hr
gross_income=basic_pay+OT_pay+hononarium
#deductions for tardy, absent
tardiness=rate_hr*hrs_day
absences=absences_hrs*rate_hr
#sss_contri
if 0 <= gross_income <= 4249.99:
    sss_contri = 180.00
elif 4250 <= gross_income <= 4749.99:
        sss_contri = 202.50
elif 4750 <= gross_income <= 5249.99:
        sss_contri = 225.00
elif 5250 <= gross_income <= 5749.99:
        sss_contri = 247.50
elif 5750 <= gross_income <= 6249.99:
        sss_contri = 270.00
elif 6250 <= gross_income <= 6749.99:
        sss_contri = 292.50
elif 6750 <= gross_income <= 7249.99:
        sss_contri = 315.00
elif 7250 <= gross_income <= 7749.99:
        sss_contri = 337.50
elif 7750 <= gross_income <= 8249.99:
        sss_contri = 360.00
elif 8250 <= gross_income <= 8749.99:
        sss_contri = 382.50
elif 8750 <= gross_income <= 9249.99:
        sss_contri = 405.00
elif 9250 <= gross_income <= 9749.99:
        sss_contri = 427.50
elif 9750 <= gross_income <= 10249.99:
        sss_contri = 450.00
elif 10250 <= gross_income <= 10749.99:
        sss_contri = 472.50
elif 10750 <= gross_income <= 11249.99:
        sss_contri = 495.00
elif 11250 <= gross_income <= 11749.99:
        sss_contri = 517.50
elif 11750 <= gross_income <= 12249.99:
        sss_contri = 540.00
elif 12250 <= gross_income <= 12749.99:
        sss_contri = 562.50
elif 12750 <= gross_income <= 13249.99:
        sss_contri = 585.00
elif 13250 <= gross_income <= 13749.99:
        sss_contri = 607.50
elif 13750 <= gross_income <= 14249.99:
        sss_contri = 630.00
elif 14250 <= gross_income <= 14749.99:
        sss_contri = 652.50
elif 14750 <= gross_income <= 15249.99:
        sss_contri = 675.00
elif 15250 <= gross_income <= 15749.99:
        sss_contri = 697.50
elif 15750 <= gross_income <= 16249.99:
        sss_contri = 720.00
elif 16250 <= gross_income <= 16749.99:
        sss_contri = 742.50
elif 16750 <= gross_income <= 17249.99:
        sss_contri = 765.00
elif 17250 <= gross_income <= 17749.99:
        sss_contri = 787.50
elif 17750 <= gross_income <= 18249.99:
        sss_contri = 810.00
elif 18250 <= gross_income <= 18749.99:
        sss_contri = 832.50
elif 18750 <= gross_income <= 19249.99:
        sss_contri = 855.00
elif 19250 <= gross_income <= 19749.99:
        sss_contri = 877.50
elif 19750 <= gross_income <= 20249.99:
        sss_contri = 900.00
else:
        sss_contri = 900.00

#Philhealth Contri
if 0 <= gross_income <= 10000.00:
    philhealth_contri = 500.00
elif 10001 <= gross_income <= 99999.99:
    philhealth_contri = gross_income * 0.05
elif gross_income > 100000.00:
    philhealth_contri = 5000.00

#withholding tax
if 0 <= gross_income <= 10417:
    withholding_tax = 0
elif 10418 <= gross_income <= 16666:
    withholding_tax = (0.00 + 15%)/10417
elif 16667 <= gross_income <= 33332:
    withholding_tax = (937.50+20%)/16667
elif 33333 <= gross_income <= 83332:
    withholding_tax = (4270.70+25%)/33333
elif 83333 <= gross_income <= 333332
    withholding_tax = (16770.70+30%)/83333
else
    withholding_tax= (91770.70+35%)/333333

#,net, total deduction
total_deduction=sss_contri+philhealth_contri+pagibig_contri+tardiness+absences
net_income=gross_income-total_deduction

#display
print("Company Name:", company_name)
print("Employee Code:",emp_code)
print("Employee Name:", emp_name)
print("Department:", department)
print("Cut-Off:", cut_off)
print("Pay Period:", pay_period)
print("Basic Pay:", basic_pay)
print("Overtime:", OT_pay)
print("Absences:",absences)
print("Hononarium:", hononarium)
print("Tardy:", tardiness)
print("Withholding Tax:",withholding_tax)
print("SSS Contribution:", sss_contri)
print("HDMF Contribution:", pagibig_contri)
print("Philhealth Contribution", philhealth_contri)
print("Deductions:", total_deduction)
print("Gross Earnings:", gross_income)
print("Net Pay:", net_income)