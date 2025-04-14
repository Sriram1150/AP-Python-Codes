def printMat(matrix):
    root = len(matrix) ** 0.5
    diff = int(root)
    if root - diff != float(0):
        raise ValueError("DimensionMismatchException")
    else:
        row = int(root)
        temp = 0
        for i in range(row):
                print([matrix[temp+j] for j in range(row)])
                temp += row

printMat([1,2,0,4,0,5,0,7,9])
printMat([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])