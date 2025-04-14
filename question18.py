def delDup(s):
    new_set = set(s)
    return sorted(list(new_set))

print(delDup([10,20,30,20,20,30,40,50,-20,60,60,-20]))