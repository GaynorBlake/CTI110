# This project is for calculating trip cost
# 27FEB2023
# CTI-110 P2HW2 - Travel
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

print(f'Location:           {destination:s}')
print(f'Initial Budget:     ${budget:.1f}')
print(f'Fuel:               ${gas:.1f}')
print(f'Accomodation:       ${lodging:.1f}')
print(f'Food:               ${food:.1f}')
print('---------------------------------------')
print()
print(f'Remaining Balance: ${remaining_balance:.1f}')
