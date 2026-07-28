import os
import sys

if os.path.exists('myfile.txt') == False:
  print('File not found named myfile.txt')
  sys.exit()

myFileVariable = open('myfile.txt', 'r')
filecontent = myFileVariable.read()
print(filecontent)
myFileVariable.close()

# # - read whole file

with open('myfile.txt', 'r') as file:
  print(file.read())

print("File is closed without close function")

# # - read first 8 bytes of file

with open('myfile.txt', 'r') as file:
  print(file.read(8))

# print("File is closed without close function")
  
# # - read file lines
with open('myfile.txt', 'r') as file:
  print("going to read first line")
  print(file.readline())
  print("going to read second line")
  print(file.readline())
  print("going to read third line")
  print(file.readline())
  print("going to close the file")
  
# print("File is closed without close function")

# # - append one line to existing file

with open('myfile.txt', 'a') as file:
  file.write("\nThis is forth line.")
  
# with open('myfile.txt', 'r') as file:
#   print(file.read())
  
# # - append one line to existing file

# with open('myfile.txt', 'w') as file:
#   file.write("I am going to re-write everything")
  
# with open('myfile.txt', 'r') as file:
#   print(file.read())

# os.remove('myfile.txt')