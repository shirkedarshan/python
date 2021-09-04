courses = ['History', 'Maths', 'Physics', 'CompScience']
print(len(courses))

courses.append('Art')
courses.insert(0, 'Drawing')
print(courses)
print(courses[0])  # starts at 0
print(courses[-1])  # returns last item
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print(courses[:])

courses_2 = ['Music', 'PT']
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('PT')
print(courses)

popped = courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)
courses.sort(reverse=True)
print(courses)

sorted(courses)  # original version of list

nums = [2, 3, 4]
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses.insert(0, 'Maths'))
print('Art' in courses)

for item in courses:
    print(item)

for index, item in enumerate(nums, start=1):
    print(index, item)

courses_str = ' - '.join(courses)
print(courses_str)

new_list = courses_str.split(' - ')
print(new_list)

# Sets
courses_set = {'Music', 'History', 'Maths', 'Physics', 'CompScience', 'Maths'}
fun_courses_set = {'Music', 'Drawing'}
print(courses_set)
print('Maths' in courses_set)
print(courses_set.intersection(fun_courses_set))
print(courses_set.difference(fun_courses_set))
print(courses_set.union(fun_courses_set))

empty_list = list()
empty_tuple = tuple()
empty_set = set()
