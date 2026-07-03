class MyClass:
  value = 10
  
  def __init__(self, initialValue):
    self.value = initialValue
  
  def printValue(self):
    print("Value that we are holding is %i" % self.value)


firstObject = MyClass(20)
firstObject.printValue()