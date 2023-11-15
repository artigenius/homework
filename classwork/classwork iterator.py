mylist = [0, 1, 2]
# создаем итератор
iterlist = iter(mylist)
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))

def for_loop (iterable, body_func):
    # iterable - итерируемый объект,
    # body_func - тело функции, какая-то мат операция или тп
    iterator = iter(iterable)
    while True: # бесконечный цикл пока нет условий остановки
        current_element = next(iterator)
        body_func(current_element)

def func(i):
    print(i ** 2)

for_loop([0,1,2], func)


def sq_numbers(n):
    for i in range(1, n+1):
        yield i**2

a = sq_numbers(3)
print('Квадраты чисел 1,2,3:')
print(next(a))
print(next(a))
print(next(a))

def get_words_starting_with_letter(text, letter):
    words = text.split()
    for word in words:
        if word[0] == letter:
            yield word

def main(): #
    text = 'The quick brown fox jumps over the lazy dog.'
    letter = 'b'
    words = get_words_starting_with_letter(text,letter)
    for word in words:
        print(word)

if __name__ == "__main__":
    main()