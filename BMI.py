# BMI
weight = int(input('Введите свой вес в килограммах: '))
height = int(input('Введите свой рост в сантиметрах: '))
BMI = weight / ((height /100) **2)
print('Индекс массы вашего тела: ', round(BMI, 2))

