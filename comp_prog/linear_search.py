def binarysearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i

    return -1

m = int(input("enter the size of array"))
print("enter the element in array ")
n=[]   
for i in range(0,m):
    n.append(int(input()))
print(n)
key = int(input("enter the element you want to search"))
k =binarysearch(n,key)
if k==-1:
    print("elemnt not present in array")
else:
    print(f"element is at{k}th position")
    