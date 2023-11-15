def add_numbers(x, y):
    """

    :param x: первое число (int)
    :param y: второе число (int)
    :return: сумма чисел x и y (int)

    """
    result = x + y
    return result

sum_result = add_numbers(3, 5)
print(sum_result)

###

def tokenizator(text):
    words = text.split()
    return words

words = tokenizator('I love you lol')
print(words)

def delete_stop (text):
    stop_words = ['lol', 'heh', 'the']
    clean_text = [i for i in text if i.lower() not in stop_words]
    return clean_text

print(delete_stop(words))

def dictionary(text):
    cleaned = delete_stop(tokenizator(text))
    freq_dict = {}
    for word in cleaned:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

print(dictionary('I love you and you love me lol we love us'))

