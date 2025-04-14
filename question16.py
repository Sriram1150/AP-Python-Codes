def extractDup(a):
    count = {}
    final = []
    for i in a:
        if i in count:
            if i not in final:
                final.append(i)
            count[i] += 1
        else:
            count[i] = 1
    return final

print(extractDup([10,20,30,20,20,30,40,50,-20,60,60,-20]))
print(extractDup([-1,1,-1,8]))
print(extractDup([-1,1,-5,8]))
