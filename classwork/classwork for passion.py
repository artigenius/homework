def get_words_from_text(text):
    tokens = text.split()
    words_seen = set()
    for word in tokens:
        if word in words_seen:
            yield word
        else:
            words_seen.add(word)

def main(): #
    text = 'She said she does not love me, she loves you. But she can not love me. But I love YOU'
    dublicates = get_words_from_text(text)
    for word in dublicates:
        print(word)

if __name__ == "__main__":
    main()
