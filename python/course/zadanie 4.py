# Fibonacci numbers, user chooses a number and program shows it according to their order
f1 = 1
f2 = 1

n = int(input("Choose a number of a digit from Fibonacci numbers: "))

i = 0
while i < n-2:
    f_sum = f1 + f2
    f1 = f2
    f2 = f_sum
    i = i + 1

print("This number equal:", f2)
input('press ENTER to exit')
