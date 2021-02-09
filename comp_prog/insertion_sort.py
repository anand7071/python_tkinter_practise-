arr=[1,11,3,2,56,23,7,89,12]
def insertionSort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertionSort(arr))