# Write a function named right_justify that takes a string named s as a parameter 
# and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    len_of_string = len(s)
    starting_point = 70 - len_of_string
    print(" " * starting_point + s)

right_justify("Epiloguer")
right_justify("is")
right_justify("cool")