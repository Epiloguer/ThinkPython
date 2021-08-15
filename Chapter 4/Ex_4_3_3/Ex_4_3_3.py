# 1. Write a function called square that takes a parameter named t, which is a turtle. It
# should use the turtle to draw a square.
# Write a function call that passes bob as an argument to square, and then run the
# program again.

# 2. Add another parameter, named length, to square. Modify the body so length of the
# sides is length, and then modify the function call to provide a second argument. Run
# the program again. Test your program with a range of values for length.

# 3. Make a copy of square and change the name to polygon. Add another parameter
# named n and modify the body so it draws an n-sided regular polygon. Hint: The
# exterior angles of an n-sided regular polygon are 360/n degrees.

import turtle

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()

polygon(bob, 100, 5)

turtle.mainloop()