# program asks for speed limit and counts the fine
speed = int(input())
speed = speed - 90 # we count the exeed number of speed
if speed >= 80:
    print ( 'Штраф составляет: 5000 рублей')
elif speed >= 60 and speed <= 80:
    print ( 'Штраф составляет: 2500 рублей')
elif speed >= 40 and speed <= 60:
    print ( 'Штраф составляет: 1500 рублей')
elif speed >= 20 and speed <= 40:
    print('Штраф составляет: 500 рублей')
else:
    print ('Скорость автомобиля допустима на данном участке')
input ('Press ENTER to exit')

