import time as t
def insertionsort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    return l


l=[]
print("this program uses insertion sort technique to sort the array elements:")
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
print("\n")
print(f"the following unsorted array is {l}")
s=insertionsort(l)
print(f"the following sorted array is {s}")
    
