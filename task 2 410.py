#Конвертер температур: программа принимает на вход температуру
#в градусах по Фаренгейту и переводит значение в градусы по Цельсию.
while True:
    x = str(input('tell me something that is not "q": '))
    x = x.lower()
    if x != 'q':
        print(f'oh, i see: {x}')
    else:
        print('bye')
        break


