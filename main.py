# Happy coding

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

s_li = sorted(li, reverse=True)
s_tup = sorted(tup, reverse=True)


print('Sorted variable :', s_li)
print('Sorted tuple :', s_tup)

print('Original variable :', li)
li.sort()
print('Original variable :', li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '{}, {}, ${}'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Strawberry', 29, 80000)
e3 = Employee('Colorful', 43, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=True)
s_employees2 = sorted(employees, key=lambda e: e.name)

print(s_employees)
print(s_employees2)