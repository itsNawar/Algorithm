num=int(input("Enter size of list: "))
list=[]
for i in range(0,num):
    user_input=int(input(f"Enter {i+1} number: "))
    list.append(user_input)

for i in range (0,len(list)):
    for k in range (0,len(list)-i-1):
        if(list[k]>list[k+1]):
            list[k],list[k+1]=list[k+1],list[k]

print ("Sorted list:",list)

