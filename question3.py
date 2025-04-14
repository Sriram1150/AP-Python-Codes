def firstLetters(str1):
    if str1[0] != ' ':
        new_str = str1[0]
    else:
        new_str = ''

    for  i in range(len(str1)):
        if str1[i] == ' ' and i != len(str1) - 1:
            new_str += str1[i+1]
    return new_str

print(firstLetters('bad is nice'))
print(firstLetters('hello other world'))
        