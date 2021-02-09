from tkinter import *
root =Tk()
root.geometry("234x234")

def bubblesort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr     

def getval():
    arr = arrayvalue.get()
    arr = arr.split(",")
    n=[]
    for i in arr:
        n.append(int(i))
    print(f"sorted array is {bubblesort(n)}")

array = Label(root, text="array")   
array.grid(row=1 , column=0)    

arrayvalue = StringVar()

arrayentry =Entry(root, textvariable=arrayvalue)
arrayentry.grid(row=1, column=1)

Button(text="submit", command=getval).grid()

root.mainloop()