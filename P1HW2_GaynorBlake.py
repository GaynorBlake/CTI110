# This project is for calculating trip cost
# 8FEB2023
# CTI-110 P1HW2 - Travel Expense
# Blake Gaynor
#

print('This program calculates and displays travel expenses')\

print('Enter Budget:', end=' ')            
budget = int(input())
print('Enter your travel destination:', end=' ')
destination = (input())      
print('How much do you think you will spend on gas?', end=' ')
gas = int(input())
print('Approximately, how much will you need for accomodation/hotel?', end='')
lodging = int(input())
print('Last, how much will you need for food?', end=' ')
food = int(input())

total_expenses = (food+lodging+gas)
remaining_balance = (budget-total_expenses)

print('------------Travel Expenses------------')

print('Location:', destination)
print()
print('Initial Budget:', budget)
print()
print('Total Expenses:', total_expenses)
print()
print('Remaining Balance:', remaining_balance)
