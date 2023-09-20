#Simple average
def average(a):
    k = 0
    m = 0
    for i in range(len(a)):
        if a[i] != 0:
            m += a[i]
            k = k + 1
    return m/k


print(average([1, 2, 3]))
print(average([2, 0, 0, 2, 2]))
print(average([2, 0, 2, 1, 1]))
input('press ENTER to exit')
