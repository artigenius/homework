# guess the number
import random

target_number = random.randint(1, 100)
number = 0
k = 0
while number != target_number:
    number = int(input('guess the number between 1 to 100: '))
    k += 1
    if number < target_number:
        print('try higher')
    elif number > target_number:
        print('try lower')
    else number == target_number:
        print(f'yes, you guessed right! it was {target_number}\nnumber of your tries: {k}'
