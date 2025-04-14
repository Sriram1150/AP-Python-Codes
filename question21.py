def moveZeros(a):
    return [i for i in a if i != 0] + [0] * a.count(0)

print(moveZeros([1,2,0,4,0,5,0]))