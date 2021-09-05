nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

print("break")

for num in nums:
    for letter in 'abc':
        print(num, letter)

print("break")

for i in range(10):
    print(i)

print("break")

for i in range(1, 11):
    print(i)

# while loop

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

while True:
    if x == 5:
        break
    print(x)
    x += 1