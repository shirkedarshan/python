"""
LEGB
Local, Enclosing, Global, Built-in
"""


import builtins
print(dir(builtins))

x = 'global x'
print(x)

# def min():
#     pass


m = min([2, 5, 1, 7, 3])
print(m)


def test(z):
    # global x
    y = 'local y'
    x = 'local x'
    # print(y)
    print(x)
    print(z)


test('local z')
# print(y)
print(x)


def outer():
    x_enclosing = 'outer enclosing x'

    def inner():
        # nonlocal x_enclosing
        x_enclosing = 'inner enclosing x'
        print(x_enclosing)

    inner()
    print(x_enclosing)


outer()
