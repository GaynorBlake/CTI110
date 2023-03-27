# CTI-110
# P3HW2 - Salary
# Blake Gaynor
# 16 March 2023

print('Enter name of employee:', end=' ')
employee_name = (input())
print('Enter hours worked:', end=' ')            
hours = float(input())     
print("What is the employee's payrate?", end=' ')
wage = float(input())
over_time_wage= wage * 1.5

if hours > 40:
    over_time_hours = hours - 40
else:
    over_time_hours= 0

if hours > 40:
    regular_hours = hours - over_time_hours
else:
    regular_hours = hours

regular_pay = regular_hours * wage

over_time_pay = over_time_hours * over_time_wage

total_pay = regular_pay + over_time_pay

print('--------------------------------------------')
print(f'Employee Name:  {employee_name}')
print()
print('Hours Worked    Pay Rate    OverTime Hours    OverTime Pay    RegHour Pay    Gross Pay')
print('---------------------------------------------------------------------------------------')
print(f'{hours:<13.1f}   {wage:<10.1f}  {over_time_hours:<17.1f} {over_time_pay:<15.2f} {regular_pay:<13.2f}  {total_pay:.2f}') 



