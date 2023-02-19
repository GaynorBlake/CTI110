import math

x= float(input())
y= float(input())
z= float(input())

output1= math.pow(x , z)
output2= math.pow(x , (y ** z))
output3= math.fabs(x - y)
output4= math.sqrt(x ** z)

print(f'{output1:.2f} {output2:.2f} {output3:.2f} {output4:.2f}')
