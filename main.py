import turtle
import math

# carl :D
turtle.colormode(255)
carl = turtle.Turtle()
carl.speed(0)
turtle.bgcolor("black")

def carlSetup(x, y):
    carl.penup()
    carl.goto(x, y)
    carl.pendown()


# window setup
wn = turtle.Screen()
wn.tracer(0)
W, H = turtle.screensize()

# different values of imaginary number c creates a different type of design
c_real = -0.8
c_imaginary = 0.156

# resolution = 2 takes around a minute and makes pizel size 2x2, resolution 1 takes 5 mins or even more
resolution = 2
# escape radius
r = 1.7


# recursion to find out how many stacks it takes for the x+yi imaginary number to escape to infinity
# the formula x**2 + y ** 2 >= r ** 2 is used to see if z
def EscapeInfinityRecursion(x, y, max_k, current_k):
    if x**2 + y**2 >= r**2 or current_k >= max_k:
        # return how much recursion it took for this pixel to exceed the condition for coloring
        return current_k
    else:
        # calculate the next set of imaginary number z (x + yi)
        x_temp = x**2 - y**2
        scaled_y = 2 * x * y + c_imaginary
        scaled_x = x_temp + c_real
        return EscapeInfinityRecursion(scaled_x, scaled_y, max_k, current_k + 1)


# progress bar variable
nextPrint = 10

# iterate through each pixel according to the resolution
for x in range(-W, W, resolution):
    for y in range(-H, H, resolution):
        scaled_x = r / W * x
        scaled_y = r / H * y

        # get the color according to the number of stacks it takes this pixel to stop
        julia_color = EscapeInfinityRecursion(scaled_x, scaled_y, 255, 0)

        # plot
        color = 255 - julia_color
        carl.pencolor(color, color, color)
        carlSetup(x, y)
        carl.dot(resolution + 2)

    # print progress
    if ((x + W) / (2 * W)) * 100 > nextPrint:
        print(f"{nextPrint}% Done")
        nextPrint += 10

wn.update()
print("100% Done")
print("Enjoy")
wn.mainloop()
