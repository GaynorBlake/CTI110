# CTI-110
# P3HW1 - Debug_List
# Blake Gaynor
# 14March2023
#

print('Enter grade for Module 1:', end=' ')            
mod1_grade = float(input())
print('Enter grade for Module 2:', end=' ')            
mod2_grade = float(input())
print('Enter grade for Module 3:', end=' ')            
mod3_grade = float(input())
print('Enter grade for Module 4:', end=' ')            
mod4_grade = float(input())
print('Enter grade for Module 5:', end=' ')            
mod5_grade = float(input())
print('Enter grade for Module 6:', end=' ')            
mod6_grade = float(input())

grade_list = [mod1_grade , mod2_grade , mod3_grade , mod4_grade , mod5_grade , mod6_grade]

avg = sum(grade_list) / len(grade_list) 

print()
print('------------Results------------')
print(f'Lowest Grade:       {min(grade_list):.1f}')
print(f'Highest Grade:      {max(grade_list):.1f}')
print(f'Sum of Grades:      {sum(grade_list):.1f}')
print(f'Average:            {avg:.2f}')
print('-------------------------------')
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

