def oddCollatz(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    result = []
    current = n
    
    if current % 2 == 1:
        result.append(current)
    
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1

        if current % 2 == 1:
            result.append(current)
    
    return result

print(oddCollatz(1))
print(oddCollatz(3))
print(oddCollatz(7))
print(oddCollatz(100))

