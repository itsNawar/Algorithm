num=int(input("Enter size of list: "))
list=[]
for i in range(0,num):
    user_input=int(input(f"Enter {i+1} number: "))
    list.append(user_input)

for j in range (0,len(list)-1):
    min_indx=j
    for k in range (j+1,len(list)):
        if(list[k]<list[min_indx]):
            min_indx=k
    list[j],list[min_indx]=list[min_indx],list[j]

print ("Sorted list:",list)

