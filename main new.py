#even-numbered
a = int(input())
if a % 2 == 0:
    print('even-numbered')
else:
    print('not even-numbered')

#can u vote??
age = int(input('enter your age = '))
if age >= 18:
    print('u can vote')
else:
    print('no u can not')

#text lenght
text = str(input())
if len(text) > 0:
    print('text lenght', len(text))
else:
    print('empty string')

#another variant
text = str(input())
if len(text) == 0:
    print('string is empty')
else:
    print(f'text len = {len(text)}')

#year cheeeeck
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

x = int(input())
if x > 20:
    print("x больше 20")
elif x > 10:
    print("x больше 10, но меньше или равно 20")
else:
    print("x меньше или равно 10")

#null or less or more
x = int(input())
if x > 0:
    print(f'{x} is positive')
elif x < 0:
    print(f'{x} is negative')
else:
    print(f'{x} is null')

#triangle
a, b, c = input().split()
if a == b == c:
    print('равносторонний')
elif a == b or b == c or c == a:
    print('равнобедренный')
else:
    print('разностороний')

#time of the year
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

if season != 'unknown':
    print(f'The season for {month} is {season}')
else:
    print(f'Error, {month} is not a month')

