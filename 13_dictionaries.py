phonebook = {}


phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
phonebook["Sagar"] = 123456789

print(phonebook)

students = {
    1: 'Sagar',
    2: 'TechCoderLabz',
    3: 'Anaiya'
}

print(students)

# -------------------

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# -----------------

for enrollmentNumber, name  in students.items():
    print("Enrollment Number %d is %s" % (enrollmentNumber, name))
    
# -----------------

if "Sagar" in phonebook:
  del phonebook["Sagar"] # phonebook.pop("Sagar") <= does the same thing

print(phonebook)

# -----------------

if 3 in students:
  print("Enrollment number 3 exists")
else:
  print("Enrollment number 3 DOES NOT exists")