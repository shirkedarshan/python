student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Comp Science']}
print(student)
print(student['courses'])
print(student.get('name', 'DATA NOT FOUND'))
student['name'] = 'Darshan'
print(student.get('name', 'DATA NOT FOUND'))

del student['age']
print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, value)
