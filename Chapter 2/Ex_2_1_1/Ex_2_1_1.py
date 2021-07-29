# We’ve seen that n = 42 is legal. What about 42 = n?

42 = n #SyntaxError: cannot assign to literal

# How about x = y = 1?

x = y = 1
print(x) # 1
print(y) # 1

# In some languages every statement ends with a semi-colon, ;. What happens if you put a 
# semi-colon at the end of a Python statement?

my_name = epiloguer; # NameError: name 'epiloguer' is not defined

# What if you put a period at the end of a statement?

my_name = epiloguer. # SyntaxError: invalid syntax

# In math notation you can multiply x and y like this: xy. What happens if you try that in 
# Python?

z = xy # NameError: name 'xy' is not defined