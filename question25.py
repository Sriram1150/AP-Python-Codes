def kMax(lst, k):
    if k > len(lst):
        raise ValueError("Exceeded current capacity")

    final = 0
    for _ in range(k):
        final = max(lst)
        lst.remove(final)
    return final

print(kMax([10,2,4,5,7,9],1))
print(kMax([10,2,4,5,7,9],2))
print(kMax([10,2,4,5,7,9],3))