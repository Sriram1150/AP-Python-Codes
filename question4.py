def evenIndexCapital(str1):
    new_str = ''
    dict1 = {'a':'A', 'b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O',
             'p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    for i in range(len(str1)):
        if 'A'<= str1[i] <= 'Z':
            raise ValueError("String should be lower case only")
        if i % 2 == 0:
            new_str += dict1[str1[i]]
        else:
            new_str += str1[i]
    return new_str

print(evenIndexCapital('school'))
