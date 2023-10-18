# Ages
age = int(input('please, enter your age: '))
if age <= 12:
    print('you are a child')
elif age > 12 and age <= 18:
    print('you are a teenager')
elif age > 18 and age <= 35:
    print('you are a youngster')
elif age > 35 and age <= 65:
    print('you are a grown up man/woman')
elif age > 65 and age <= 116:
    print('you are en elder')
elif age > 116:
    print('you are lying >:(')
