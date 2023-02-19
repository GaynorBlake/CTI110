

user_num= float(input())
div_num= float(input())

your_value1= user_num / div_num
your_value2= user_num / (div_num * div_num)
your_value3= int(user_num / (div_num * div_num * div_num))

print(f'{your_value1:.0f} {your_value2:.0f} {your_value3:.0f}')
