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
    super().showInfo()
    print(f"Fuel type for {self.model} is {self.fuelType}")

aGenericVehicle = Vehicle(80, "Suzuki Ciaz")
aGenericVehicle.updateSpeed(70)
aGenericVehicle.showInfo()


suzukiAlto = Car(60, 'Alto', 'Petrol')
suzukiAlto.showInfo()

firstObject = MyClass(20)
firstObject.printValue()