a = [[2, -2], [5, 3]]
b = [[-1, 4], [7, -6]]
 
# newarr = []
# temparr = []

# temparr.append((a[0][0] * b[0][0]) + (a[0][1] * b[1][0]))
# temparr.append((a[0][0] * b[0][1]) + (a[0][1] * b[1][1]))

# newarr.append(temparr)
# temparr=[]

# temparr.append((a[1][0] * b[0][0]) + (a[1][1] * b[1][0]))
# temparr.append((a[1][0] * b[0][1]) + (a[1][1] * b[1][1]))

# newarr.append(temparr)

newarr = [[0 for y in range(len(b[0]))] for x in range(len(a))]

for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a[0])):
            newarr[i][j] += a[i][k] * b[k][j]


print(newarr)