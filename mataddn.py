arr1 = [[1, 3], [2, 4]]
arr2 = [[5, 2], [1, 0]]
 
newarr = []
temparr = []

for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        temparr.append(arr1[i][j] + arr2[i][j])
    newarr.append(temparr)
    temparr=[]

print(newarr)