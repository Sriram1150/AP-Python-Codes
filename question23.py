def matMul(m1,m2):
    main1 = m1
    main2 = m2
    root1 = len(m1) ** 0.5
    diff1 = int(root1)
    root2 = len(m2) ** 0.5
    diff2 = int(root2)
    if root1 - diff1 != float(0) or root2 - diff2 != float(0) or root1 != root2:
        raise ValueError("DimensionMismatchException")
    m1 = [[0]*diff1 for _ in range(int(root1))]
    m2 = [[0]*diff1 for _ in range(int(root1))]

    num = int(root1)

    temp1 = 0
    for i in range(num):
        for j in range(num):
            m1[i][j] = main1[temp1]
            temp1 += 1
    
    temp2 = 0
    for i in range(num):
        for j in range(num):
            m2[i][j] = main2[temp2]
            temp2 += 1
    final = [[0]*num for _ in range(num)]

    for i in range(num):
        for j in range(num):
            for k in range(num):
                final[i][j] += m1[i][k] * m2[k][j]
    final2 = []

    for i in final:
        final2 += i
    return final2


print(matMul([1,2,0,4,0,5,0,7,9],[1,2,0,4,0,5,0,7,9]))