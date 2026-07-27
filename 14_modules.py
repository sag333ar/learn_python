import maths as adityas_maths_functions

a = int(input())
b = int(input())

obj = adityas_maths_functions.MyClass(30)
obj.printValue()

print("from another file, we are calling add function - %d" % adityas_maths_functions.add(a, b))
print("from another file, we are calling sub function - %d" % adityas_maths_functions.sub(100, 40))
print("from another file, we are calling div function - %d" % adityas_maths_functions.div(50, 25))
print("from another file, we are calling div function - %d" % adityas_maths_functions.mul(50, 25))