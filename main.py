a = [0, 0, 0]
b = [1, 1, 1]
c = [2, 2, 2]

a, b, c = c, a, b
print(a, b, c)

full_name = ["John", "Smith"]
name, surname = full_name
print(name, surname)

full_name = "John Smith"
name, surname = full_name.split()
print(name, surname)

numbers = '1, 2, 3'
nenumbers = numbers.split(',')
print (nenumbers)

test = 'this is a sentence'
test = test.split(' ')
for i in test:
    print (i)

new = [1,2,3]
for i in new:
    print(0) #делаем счетчики

n = 0
for i in new:
    n = n + 1
    print (n)

name = 'john'
surname = 'smith'
age = 30
*data, = name, surname, age
print (data)

*a, b = data
print(a, b)

print(val := 11)

a = int(input())
b = int(input())
s = (a * b) / 2
print (s)

