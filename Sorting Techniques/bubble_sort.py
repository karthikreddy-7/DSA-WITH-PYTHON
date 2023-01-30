import time as t

def bubblesort(l):
    e=sorted(l)
    for j in range(len(l)):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp
            print(f"{l}\n")
            if l==e:
                print("the array is sorted")
                return l
                break


l=[]
print("this program uses bubble sort technique to sort the array elements:")
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
s=bubblesort(l)
print(f"the following sorted array is {s}")
    