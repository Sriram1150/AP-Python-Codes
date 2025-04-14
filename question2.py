def minIndexFirstString(str1, str2):
    index = -1
    for i in range(len(str1)):
        if str1[i] in str2:
            index = i
    return index

print(minIndexFirstString('tiger','integer'))
print(minIndexFirstString('integer','tiger'))
        
