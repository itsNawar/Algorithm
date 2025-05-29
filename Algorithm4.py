def merge(list,l,m,r):
    n1=m-l+1
    n2=r-m

    left=list[l:m+1]
    right=list[m+1:r+1]

    i=j=0
    k=l

    while(i<n1 and j<n2):
        if(left[i]<=right[j]):
            list[k]=left[i]
            i=i+1
        else:
            list[k]=right[j]
            j=j+1
        k=k+1

    while(i<n1):
       list[k]=left[i]
       i=i+1
       k=k+1

    while(j<n2):
       list[k]=right[j]
       j=j+1
       k=k+1

def mergeSort(list,l,r):
    if(l<r):
        m=(l+r)//2
        mergeSort(list,l,m)
        mergeSort(list,m+1,r)
        merge(list,l,m,r)


num=int(input("Enter size of list: "))
list=[]
for i in range(0,num):
    user_input=int(input(f"Enter {i+1} number: "))
    list.append(user_input)

mergeSort(list,0,num-1)

print ("Sorted list:",list)
