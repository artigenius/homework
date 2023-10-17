string = 'python'
for i in string:
    print(i)

num = 123456789
for i in str(num):  # change data type
    print(i)

text = 'This is a sample sentence'
for i in text.split():
    print(i)

names = ['Masha', 'Dasha', 'Pasha']
for i in names:
    print('Hello, ' + i)

names = ['Masha', 'Dasha', 'Pasha']
for i in names:
    print(f'Hello, {i}')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for elem in matrix:
    for digit in elem:
        print(digit)

stroke = 'Hello, it is me, I was wondering'
dic = 'aeiou'
count = 0
for char in stroke.lower():
    if char in dic:
        count += 1
print('num of vowels', count)

for i in range(4):
    print(i)

for i in range(2, 9, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(1, 50, 2):
    print(i)

number = 5
factorial = 1
for i in range(1, number + 1):  # to count further than number
    factorial *= i
    print(factorial)

# multiply table
num = 3
for i in range (1, 10):
    print(f'{num} X {i} = {num * i}')

