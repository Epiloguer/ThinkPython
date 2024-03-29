#1. Write a function called square that takes a parameter named t, which is a turtle. It
# should use the turtle to draw a square.
# Write a function call that passes bob as an argument to square, and then run the
# program again.
 
# 2. Add another parameter, named length, to square. Modify the body so length of the
# sides is length, and then modify the function call to provide a second argument. Run
# the program again. Test your program with a range of values for length.
 
# 3. Make a copy of square and change the name to polygon. Add another parameter
# named n and modify the body so it draws an n-sided regular polygon. Hint: The
# exterior angles of an n-sided regular polygon are 360/n degrees.
 
# 4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
# that draws an approximate circle by calling polygon with an appropriate length and
# number of sides. Test your function with a range of values of r.
# Hint: figure out the circumference of the circle and make sure that length * n =
# circumference.

import turtle
import math

bob = turtle.Turtle()

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)        

circle(bob, 200)

turtle.mainloop()