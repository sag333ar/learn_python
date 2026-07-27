def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def div(a, b):
  return a / b

def mul(a, b):
  return a * b

class MyClass:
  def __init__(self, initialValue):
    self.value = initialValue
  
  def printValue(self):
    print("Value that we are holding is %i" % self.value)

def main():
  print("testing maths add function - %d" % add(10, 20))
  
if __name__ == '__main__':
    main()