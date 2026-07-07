x = 2
myFloatValue = 75.754545
firstName = "Sagar"

if x == 1 or firstName == "Sir":
  print("x is holding a value %d" % x)
else:
  print("x is something else %d" % x)
  print("aditya inside else scope")

print("Percent %f" % myFloatValue)
print("int value %i float value %.2f string value %s" % (x, myFloatValue, firstName))
print(f"int value {x}, float value {myFloatValue}, string value {firstName}")