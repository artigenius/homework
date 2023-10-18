# конвертер оценок
a = int(input('Please, enter your grade from 1 to 10: '))
if a <= 2:
    grade = 'D = non-satisfactory'
elif a <= 5 and a > 2:
    grade = 'C = satisfactory'
elif a > 5 and a <= 8:
    grade = 'B = very good'
elif a >= 9:
    grade = 'A = excellent'
else:
    grade = 'unknown'

if grade != 'unknown':
    print(f'Your grade is {grade}, nice job!')
else:
    print('Error, try again')
