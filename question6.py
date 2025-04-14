def distChar(str1,str2):
    unique_str = []
    temp_dict = {}

    for i in str1:
        temp_dict[i] = 1
    for i in str2:
        if i in temp_dict:
            temp_dict[i] = 0
        else:
            temp_dict[i] = 1
    
    for c in str1:
        if temp_dict[c] == 1 and c not in unique_str:
            unique_str.append(c)
    for c in str2:
        if temp_dict[c] == 1 and c not in unique_str:
            unique_str.append(c)
    
    for i in range(len(unique_str)):
        for j in range(i+1,len(unique_str)):
            if unique_str[i] > unique_str[j]:
                unique_str[i],unique_str[j] = unique_str[j],unique_str[i]
    
    finalstr = ''
    for i in unique_str:
        finalstr += i

    return finalstr


print(distChar('characters','alphabets'))
print(distChar('apples','oranges'))
print(distChar('apples','apples'))
