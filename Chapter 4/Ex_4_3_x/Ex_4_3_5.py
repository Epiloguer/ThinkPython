# Make a more general version of circle called arc that takes an additional parameter
# angle, which determines what fraction of a circle to draw. angle is in units of degrees,
# so when angle=360, arc should draw a complete circle.

import turtle
import math

bob = turtle.Turtle()

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)        

arc(bob, 200)

turtle.mainloop()