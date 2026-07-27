class MyClass:
  def __init__(self, initialValue):
    self.value = initialValue
  
  def printValue(self):
    print("Value that we are holding is %i" % self.value)

class Vehicle:
  def __init__(self, maxSpeed, name):
    self.__speed = maxSpeed
    self.model = name
  
  def showInfo(self):
    print(f"{self.model} is having max speed of {self.__speed}")
  
  def updateSpeed(self, newSpeed):
    self.__speed = newSpeed

class Car(Vehicle):
  def __init__(self, maxSpeed, name, fuelType):
    super().__init__(maxSpeed, name)
    self.fuelType = fuelType
    
  def showInfo(self):
    print("========")
    super().showInfo()
    print(f"Fuel type for {self.model} is {self.fuelType}")

aGenericVehicle = Vehicle(80, "Suzuki Ciaz")
aGenericVehicle.updateSpeed(70)
aGenericVehicle.showInfo()


suzukiAlto = Car(60, 'Alto', 'Petrol')
suzukiAlto.showInfo()

windsor = Car(40, 'Windsor', 'Electric')
windsor.showInfo()

firstObject = MyClass(20)
firstObject.printValue()


# ==========

class Student2:
  def helloWorld():
    print("Hello World")

studentObject = Student2()
studentObject.helloWorld()

# ==========

class Student:
  def __init__(self, name, age, no):
    self.__name = name
    self.__age = age
    self.__no = no
  
  def display(self):
    print(f"{self.__name} | {self.__age} | {self.__no}")
  
  def upgrade(self):
    self.__age = 1 + self.__age 

harshal = Student("Harshal", 23, 10)
harshal.display()
harshal.upgrade()
harshal.display()