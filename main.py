# object identity -> is
language = 'python'

if language == 'python':
    print("If condition is true, language is python")
elif language == 'Java':
    print("Java is the language")
else:
    print("Else condition")

logged_in = True

if language == 'python' and logged_in:
    print("Passed")
else:
    print('Bad words')

if not logged_in:
    print("Please log in")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

b = a
print(a is b)

condition = {}

if condition:
    print("Evluated to true")
else:
    print("Evluated to false")
