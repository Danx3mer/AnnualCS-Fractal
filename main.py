import turtle
import math

#carl :D
turtle.colormode(255)
carl = turtle.Turtle()
carl.speed(10)
turtle.bgcolor("red")

def carlSetup(x, y):
    carl.penup()
    carl.goto(x, y)
    carl.pendown()

c_real = 0.285
c_imaginary = 0.01
wn = turtle.Screen()
wn.tracer(0)

r = 2
W, H = turtle.screensize()
for x in range(-W // 2, W // 2):
    for y in range(-H // 2, H // 2):
        scaled_x = r/W * x
        scaled_y = r/H * y

        iteration = 0
        max_iter = 255

        while(scaled_x ** 2 + scaled_y ** 2 < r ** 2 and iteration < max_iter):
            x_temp = scaled_x ** 2 - scaled_y ** 2
            scaled_y = 2 * scaled_x * scaled_y + c_imaginary
            scaled_x = x_temp + c_real

            iteration = iteration + 1

        
        #if iteration == max_iter:
        carl.pencolor(iteration, iteration, iteration)
        carlSetup(x, y)  
        carl.dot(4)
        print(iteration)
wn.update()
wn.mainloop()
input()
