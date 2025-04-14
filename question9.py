def moveDups(s):
    dups = ''
    non_dups = ''

    for i in s:
        if i not in non_dups:
            non_dups += i
        else:
            dups += i
    
    return non_dups + '_' + dups

print(moveDups('cartoon'))
print(moveDups('network'))
print(moveDups('aabbcc'))
print(moveDups('cccbbaaa'))
        