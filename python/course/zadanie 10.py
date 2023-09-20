#longest word in a phrase
def longest_word (a) :
    return max(a.split(), key=len)

print(longest_word(input()))
input('press ENTER to exit')