# user has to guess the random number the computer has chosen
import random
print('guess the number from 1 to 10')
n = random.randint(1, 10) # computer chooses the number
n1 = int(input()) # user guesses the number
count = 1 # as user has already guessed once
while n1 != n: # if the guess is not correct
    if n1 > n:
        print('your guess - ', n1, 'is higher than the number')
        count = count + 1  # we add 1 to the count
    else:
        print('your guess - ', n1, 'is lower than the number')
        count = count + 1
    n1 = int(input('guess again: ')) # here we suggest user to try loop again
print(n1, 'your guess is right!', count, '- the number of guesses')
input('press ENTER to exit')

