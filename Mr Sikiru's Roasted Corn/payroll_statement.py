def employee_name():
    name = input("Enter employee's name: ")
    return name

def hours_worked():
    hours = float(input("Enter number of hours worked in a week: "))
    return hours

def hourly_pay_rate():
    pay_rate = float(input("Enter hourly pay rate: "))
    return pay_rate

def month():
    month_worked = input("Enter month worked: ")
    return month_worked

def federal_withholding_tax():
    federal_rate = float(input("Enter federal tax withholding rate: "))
    return federal_rate

def state_withholding_tax():
    state_tax = float(input("Enter state tax withholding rate: "))
    return state_tax


employee = employee_name()
hour = hours_worked()
pay = hourly_pay_rate()
month_of_work = month()

gross_pay = hour * pay

federal_tax_rate = federal_withholding_tax()
federal_tax = (federal_tax_rate / 100) * gross_pay

state_tax_rate = state_withholding_tax()
state_tax = (state_tax_rate / 100) * gross_pay

total_deduction = federal_tax + state_tax
net_pay = gross_pay - total_deduction

print("\n================================================================")
print(f" {employee} Payroll statement for the month of {month_of_work}")
print("----------------------------------------------------------------")
print(f"""Employee Name: {employee}
Hours Worked: {hour}
Pay Rate: ${pay}
Gross Pay: ${gross_pay}
Deductions:
Federal Withholding ({federal_tax_rate}%): ${federal_tax}
State Withholding ({state_tax_rate}%): ${state_tax}
Total Deduction: ${total_deduction}
Net Pay: ${net_pay:.2f}
================================================================""")

