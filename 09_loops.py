# -- In Loop

numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
    
# ------------------------

# -- In Range Loop - 1

print('----') # separator from previous output
print('In Range Loop - 1')
# following is equivalent to for(i = 0; i < 5; i++)
for i in range(5):
    print(i)
    
# ------------------------

# -- In Range Loop - 2

# from 5 to 10 or for(i = 5; i < 10; i++)
print('----') # separator from previous output
print('In Range Loop - 2')
for x in range(5, 10):
    print(x)
    
# ------------------------

# -- In Range loop - 3
    
# Prints out 0, 2, 4, 6, 8 but not 10
# equivalent to for(i = 0; i < 10; i+=2)
print('----') # separator from previous output
print('In Range Loop - 3')
for x in range(0, 10, 2):
    print(x)
    
# ------------------------

# -- In Range loop - 4 - continue example

# Prints out only odd numbers - 1,3,5,7,9
print('----') # separator from previous output
print('In Range Loop - 4')
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# ------------------------

# -- In Range loop - 5 - normal exit & upon exit

# Prints out only odd numbers - 1,3,5,7,9
print('----') # separator from previous output
print('In Range Loop - 5')
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
else:
    print('x is now %d' % x)

# ------------------------
    
# -- While Loop with break

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count = count + 1
    if count >= 5:
        break
    
# ------------------------

