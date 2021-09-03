message = "Hello strawberry"
multiline_message = """ This is
multiline message that
we can write in one variable
with three ' """

print("Hello python")
print(multiline_message)
print("len(multiline_message) -> " + str(len(multiline_message)))
print("message : " + message)
print("message[0] -> " + message[0])
print("message[0:5] -> " + message[0:5])
print("message[:5] -> " + message[:5])
print("message[6:] -> " + message[6:])
print("message.lower() -> " + message.lower())
print("message.count(Hello) -> " + str(message.count('Hello')))
print("message.count(l) -> " + str(message.count('l')))
print("message.find('python') -> " + str(message.find('python')))
print("message.find('s') -> " + str(message.find('s')))

greeting = "Hello"
name = "senorita"

greeting_message = greeting + ', ' + name
print(greeting_message)

replaced_string = message.replace('strawberry', 'monkey')
print(replaced_string)

first_name = "first_name"
last_name = "last_name"
dynamic_message = '{}, {}. Welcome'.format(first_name, last_name)
fstring_message = f'{first_name}, {last_name} . Welcome'

print(dynamic_message + fstring_message)
print(dir(first_name))
print(help(str))