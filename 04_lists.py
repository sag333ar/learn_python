listForNumbers = []
listForNumbers.append(1)
listForNumbers.append(2)
listForNumbers.append(3)
listForNumbers.append(4)
listForNumbers.append(5)
listForNumbers.append("Hello")
listForNumbers.append(7.777)
print(listForNumbers)

anotherList = ['Sagar', 'TechCoderLabz', 'Pune', 'MH']

for eachValue in listForNumbers:
  if type(eachValue) == int:
    print("∙ %d" % eachValue)
  elif type(eachValue) == float:
    print("* %f" % eachValue)
  else:
    print("- %s" % eachValue)