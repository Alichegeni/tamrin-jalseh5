import turtle
import time
import math
pi = math.pi

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

win = turtle.Screen()
pen = turtle.Pen()
pen.shape('turtle')
x = -20
size = 100


for i in range(1, 7):
    
    for j in range(i+2):
        
        pen.forward(size)
        pen.left(float(360 / (i+2) ))
        Height = float(100 / 2 * math.tan(pi / i+2))
    
    print(Height, '||', pen.pos())

  
    pen.penup()
    pen.setpos(i, x)
    pen.goto(i-8 , x)   
    pen.pendown()
    x -= 20
    size += 15    
win.mainloop()
    

time.sleep(10)