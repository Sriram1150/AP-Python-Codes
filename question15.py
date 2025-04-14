def subPali(s):

    def checkPalindrome(s):

        i,j = 0, len(s) - 1 

        is_palindrome = True
        while i < j:
            if s[i] != s[j]:  
                is_palindrome = False
                break
            i += 1
            j -= 1

        if is_palindrome:
            return True 
        else:
            return False
        
    n = len(s)

    bool_sub = []
    total_subs = []

    for i in range(1,n+1):
        number_of_sub = n - i + 1
        subs1 = []
        subs2 = []
        for j in range(number_of_sub):
            subs1.append(checkPalindrome(s[j:j+i]))
            subs2.append(s[j:j+i])
        bool_sub.append(subs1)
        total_subs.append(subs2)
    maxsub = 0
    for i in range(len(bool_sub)):
        if True in bool_sub[i]:
            maxsub = i+1
    return maxsub
print(subPali('bbbabcbabdfb'))
print(subPali('abcdefg'))

