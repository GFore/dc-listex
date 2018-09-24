arr1 = [2, 3, 4, 5]
arr2 = [1, 2, 3, 4]
 
newarr = []

for i in range(len(arr1)):
    newarr.append(arr1[i] * arr2[i])

print(newarr)