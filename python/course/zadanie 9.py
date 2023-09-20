#the longest string
def unique_string(string):
    list_uni_str = []
    subst = ''
    for i in string:
        if i not in subst:
            subst += i
            if subst not in list_uni_str:
                list_uni_str.append(subst)
    print(max(list_uni_str, key = len))

unique_string(input())



