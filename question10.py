def seperate(s):
    temp = {}
    final = []
    for i in s:
        if i not in temp:
            temp[i] = i
        else:
            temp[i] += i
    for i in temp.values():
        final.append(i)
    
    return final

print(seperate('cartoon'))
print(seperate('network'))
print(seperate('aabbcc'))
print(seperate('cccbbaaa'))
        
    