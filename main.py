# import my_module
from my_module import find_index as fi, test
import sys
import random
import math
import datetime
import calendar
import os

courses = ['History', 'Maths', 'Physics', 'CompSci']
# index = find_index(courses, 'Maths')
index = fi(courses, 'Maths')

print(index)
print(test)
print(sys.path)
print("sys.path.append(('<Actual path of module>')))")

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(f"Today : {today}")

print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)