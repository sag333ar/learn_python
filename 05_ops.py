number = 5 + 3 * 3 / 4.0
print(number)

# -------

left = 17 % 5 # remainder
print(left)

# -------

power2 = 7 ** 2 # power 2
power3 = 2 ** 3 # power 3
print(power2)
print(power3)

# -------

lostsOfAdityas = "Aditya " * 5 # join 5 times same string
print(lostsOfAdityas)

# -------

even = [2,4,6,8]
odd = [1,3,5,7]
# Join two arrays into one
all = even + odd
print(all)

# -------

print(odd * 3) # make one array by joining same array multiple times

# -------

print("This is odd list - %s" % odd) # use %s to show value of a list in string

# -------
format = "this is odd %s, this is even %s"
print(format % (odd, even))