def bsearch(l,key):
    count=0
    l.sort()
    count=0
    lb=0
    ub=len(l)
    mid=(lb+ub)//2
    for i in range((2*n)):
        mid=(lb+ub)//(2)
        if key==l[mid]:
            print("The element has been found at {} index of the list".format(mid))
            print("the operation took {} rounds.".format(i+1))
            print("the Lower and Upper bond for the final operation was {} and {} ".format(lb,ub))
            count=1
            break
        if key<l[mid]:
            ub=mid-1
        if key>l[mid]:
            lb=mid+1
    if count==0:
        print("the element does not exist in the list")
    return 0

def lsearch(l,key):
    count=0
    for i in range(n):
        if key==l[i]:
            print("the key value has been found at {} index of the list".format(i))
            count=1
    if count==0:
        print("the element has not been found.")
    print("the elements are {} ".format(l))
    return 0


n=int(input("enter the number of elements:"))
l=[]
for i in range(n):
   x=int(input("enter the {} index number: ".format(i)))
   l.append(x)
key=int(input("enter the key value:"))
print("the elements are {} ".format(l))
q=int(input("enter 1 for binary search and 0 for linear search:"))
if q==1:
    bsearch(l,key)
elif q==0:
    lsearch(l,key)
else:
    print("please enter the correct value of operation")
