# CTI-110
# P4HW2 - Salary Calculator
# Blake Gaynor
# 15 April 2023



employee_data = []
done = False

while not done:
    print('Enter name of employee or "Done" to terminate:', end = ' ')
    employee_name = input()
    if employee_name.lower() == 'done':
        done = True
    else:
        print('How many hours did', employee_name, 'work?', end = ' ')
        hours = float(input())
        print('What is', employee_name, 'payrate?', end = ' ')
        wage = float(input())
        over_time_wage = wage * 1.5

        if hours > 40:
            over_time_hours = hours - 40
        else:
            over_time_hours = 0

        if hours > 40:
            regular_hours = hours - over_time_hours
        else:
            regular_hours = hours

        regular_pay = regular_hours * wage

        over_time_pay = over_time_hours * over_time_wage

        total_pay = regular_pay + over_time_pay

    
        employee_data.append({
            'name': employee_name,
            'hours': hours,
            'wage': wage,
            'regular_hours': regular_hours,
            'over_time_hours': over_time_hours,
            'regular_pay': regular_pay,
            'over_time_pay': over_time_pay,
            'total_pay': total_pay
        })
        print()
        print(f'Employee Name:  {employee_name}')
        print()
        print('Hours Worked     Pay Rate    OverTime Hours   OverTime Pay    RegHour Pay    Gross Pay')
        print('---------------------------------------------------------------------------------------')
        print(f'{hours:<14.1f}   {wage:<10.2f}  {over_time_hours:<16.1f} {over_time_pay:<15.2f} {regular_pay:<14.2f} {total_pay:.2f}')
        print()

total_employees = len(employee_data)
total_regular_pay = sum([emp['regular_pay'] for emp in employee_data])
total_over_time_pay = sum([emp['over_time_pay'] for emp in employee_data])
total_gross_pay = sum([emp['total_pay'] for emp in employee_data])

    
print()
print('Total number of employees entered:', total_employees)
print('Total amount paid for the overtime:', total_over_time_pay)
print('Total amount paid in regular hours:', total_regular_pay)
print('Total amount paid in gross:', total_gross_pay)


