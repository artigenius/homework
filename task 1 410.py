#Индекс массы тела: программа принимает
#на вход вес пользователя в килограммах
#и рост в сантиметрах.
#Посчитать индекс массы тела
#пользователя, записать его в
#переменную и вывести на экран.

print ('Введите свой вес в килограммах: ')
ves = int(input())
print ('Введите свой рост в сантиметрах: ')
rost = int(input())
print ('Индекс массы вашего тела: ', ves / ((rost / 100) **2) )