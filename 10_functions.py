# Define our 3 functions
def hello_world():
    print("Hello world!")

def greetings(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
hello_world()

greetings("Sagar Kothari", "a great year!")
greetings(1, 2)

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

print(sum_two_numbers("Sagar", "Python"))