def delVowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new_str = ''
    for i in s:
        if i not in vowels:
            new_str += i
    return new_str

print(delVowels('SfgEtfjofubjiekp'))
print(delVowels('aEiOu'))