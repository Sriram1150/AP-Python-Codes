def minOp(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 >= len2:
        count = len1 - len2
        for i in range(len(str2)):
            if str2[i] != str1[i]:
                count += 1
    else:
        count = len2 - len1
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
    return count

print(minOp('python','pythons'))
print(minOp('abc',''))
print(minOp('abc','def'))  
print(minOp('ab','def'))  