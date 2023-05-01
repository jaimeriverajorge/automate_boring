# This script creates a simple dictionary
# and demonstrates the methods get() and setdefault()

student = {'name': 'jorge', 'age': 24, 'color':'blue'}

myKeys = list(student.keys())

print(myKeys)

print(student)

name = student.get('name', '')

print(name)

subject = student.get('subject', 'none')
print(subject)

gpa = student.setdefault('gpa', 3.0)
print(gpa)
print(student)
