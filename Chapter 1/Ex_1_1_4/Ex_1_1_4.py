# In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
# What about 011?

x = 09
print(x) #SyntaxError: leading zeros in decimal integer literals are not permitted;
            # use an 0o prefix for octal integers

x = 011
print(x) # Same error as above.