print("print function")

print(abs(-30))

print(len('Hello World!'))

print(bool(0)) # false
print(bool(1)) # true
print(bool(100)) # true
print(bool('Hello')) # true
print(bool(None)) # false

print(dir('Aditya'))
list = [1, 3, 4]
print(dir(list))
# print(help('aditya'.center))

mycode = "print(len('Hello World!'))"
eval(mycode)
exec(mycode)

print(10 + int("20"))
print("Hello " + str(30))
print("Hello ", (float("1234.34") + float("22.23")))