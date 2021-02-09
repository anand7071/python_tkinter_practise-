arr = [19,16,2,8,11,12,3]
temp=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
