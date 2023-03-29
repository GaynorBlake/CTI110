import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

t.pensize(6)            
t.pencolor("purple")     
t.shape("square")


for i in (1,2,3,4):
    t.forward(100)
    t.left(90)
    
t.pensize(3)            
t.pencolor("green")     
t.shape("triangle")
    

for i in (1,2,3,4,):
    t.forward(100)
    t.right(120)

win.mainloop()
