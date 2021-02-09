arr=[1,9,2,15,17,3]
n=[]
for i in range(len(arr)):
    m=min(arr)
    arr.remove(m)
    n.append(m)
print(n)