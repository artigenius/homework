#foreign passport
dic = {"а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"e", "ё":"e",
       "ж":"zh", "з":"z", "и":"i", "й":"i", "к":"k", "л":"l", "м":"m",
       "н":"n", "о":"o", "п":"p", "р":"r", "с":"s", "т":"t", "у":"u",
       "ф":"f", "х":"h", "ц":"ts", "ч":"ch", "ш":"sh", "щ":"shch",
       "ъ":"ie", "ы":"y", "ь":"", "э":"e", "ю":"iu", "я":"ia", " ":" "}

print('Write your name: ')
name = str(input())
name1 = str.lower(name)
name_eng = str()

len_name1 = len(name1)
for i in range(0, len_name1):
    name_eng = name_eng + dic[name1[i]]

print(name_eng.title())
input('press ENTER to exit')