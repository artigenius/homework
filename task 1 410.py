month = str(input('enter the name of the month:'))
month = month.lower()
if month in ['december', 'january', 'febrary']:
    season = 'winter'
elif month in ['september', 'october', 'november']:
    season = 'autumn'
elif month in ['june', 'july', 'autumn']:
    season = 'summer'
elif month in ['mai', 'april', 'mars']:
    season = 'spring'
else:
    season = 'unknown' #непредусмотренный случай

<<<<<<< HEAD
if season != 'unknown':
    print(f'The season for {month} is {season}')
else:
    print(f'Error, {month} is not a month')
=======
weight = int(input('Введите свой вес в килограммах: '))
height = int(input('Введите свой рост в сантиметрах: '))
BMI = weight / ((height /100) **2)
print('Индекс массы вашего тела: ', round(BMI, 2))
>>>>>>> 9a88ecc5b15255b4ae6aacc5ad211d07aef1ad6c
