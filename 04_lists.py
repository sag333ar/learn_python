intListForNumbers = []
intListForNumbers.append(1)
intListForNumbers.append(2)
intListForNumbers.append(3)
intListForNumbers.append(4)
intListForNumbers.append(5)
intListForNumbers.append("Hello")
intListForNumbers.append(7.777)
print(intListForNumbers)

for eachValue in intListForNumbers:
  if type(eachValue) == int:
    print("∙ %d" % eachValue)
  elif type(eachValue) == float:
    print("* %f" % eachValue)
  else:
    print("- %s" % eachValue)