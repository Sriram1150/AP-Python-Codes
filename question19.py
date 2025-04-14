def weave(a,b):
    if len(a) != len(b):
        raise ValueError("Both list not equal lenght")
    return(a+b)

print(weave([],[]))
print(weave([1,2,3],[4,5,6]))