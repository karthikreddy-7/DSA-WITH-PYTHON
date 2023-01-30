
import time as t
def selectionsort(l):
    e=sorted(l)
    firstindex=0
    for i in range(len(l)):
        minimum=l[firstindex]
        for i in range(firstindex,len(l)):
            if minimum>l[i]:
                minimum=l[i]
        k=0
        print(f"the minimum for the {firstindex} step is {minimum}\n")
        for i in range(len(l)):
            if minimum==l[i]:
                k=i
        temp=l[firstindex]
        l[firstindex]=minimum
        l[k]=temp
        firstindex=firstindex+1
    return l


l=[]
print("this program uses selection sort technique to sort the array elements:")
t.sleep(2)
print("enter the elements of the array one by one, when finished press blank")
y=input("enter the element :")
while y!="":
    x=int(y)
    if y.isnumeric==False:
        print("enter the valid value")
    else:
        l.append(x)
    y=input("enter the element: ")
print(f"the following unsorted array is {l}")
s=selectionsort(l)
print(f"the following sorted array is {s}")
    