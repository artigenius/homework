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
