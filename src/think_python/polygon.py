import turtle
import math


'''
bob.pd()
for i in range(4):
    bob.fd(100)
    bob.lt(90)
# end for
turtle.mainloop()
'''


# Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square. 
# Write a function call that passes bob as an argument to square, and then run the program again.
'''
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    # end for
    return

square(bob)
'''

# Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a 
# second argument. Run the program again. Test your program with a range of values for length.
'''
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    # end for
    return
square(bob, length = 250)
'''

# Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. 
# Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

def polyline(t, sides, length, angle):
    for i in range(sides):
        t.fd(length)
        t.lt(angle)
    # end for
    return

def polygon(t, length, sides):
    angle = 360 / sides
    polyline(t, sides, length, angle)
    return
# polygon(bob, length = 50, sides = 5)

# Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle by calling polygon with 
# an appropriate length and number of sides. Test your function with a range of values of r. 
# Hint: figure out the circumference of the circle and make sure that length * n = circumference.

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    sides = int(arc_length / 3) + 1
    step_length = arc_length / sides
    step_angle = angle / sides
    polyline(t, sides, step_length, step_angle)
    return


def circle(t, radius):
    arc(t, radius, 360)
    return

def square(t, length):
    sides = 4
    polygon(t, length, sides)
    return

def triangle(t, length):
    sides = 3
    polygon(t, length, sides)
    return

def main():
    bob = turtle.Turtle()
    # arc(bob, 100, 180)
    # square(bob, 50)
    triangle(bob, 100)
    return

if __name__ == '__main__':
    main()


    