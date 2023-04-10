print('How Many Scores do you want to enter?', end = '')
num_grades = int(input())

grade_list = []
for x in range (1, num_grades + 1, 1):
    print('Enter score #', x, ':', end=" ")
    num = float(input())

    if  0 <= num <= 100:
        grade_list.append(num)
    else:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        print('Enter score #', x, ':', end=" ")
        num = float(input())
        grade_list.append(num)
        
            




print()
print('------------Results------------')
print(f'Lowest Grade:       {min(grade_list):.1f}')
lowest = min(grade_list)
grade_list.remove(lowest)
grade_list.sort()
print(f'Modified List:', end = ' ')
print(grade_list)

total = sum(grade_list)

length = len(grade_list)

average = total / length
print(f'Scores Average:     {(average):.1f}')

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'Grade:', end = ' ')
print(grade)
print('-------------------------------')

