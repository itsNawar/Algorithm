num=int(input("Enter size of list: "))
list=[]
for i in range(0,num):
    user_input=int(input(f"Enter {i+1} number: "))
    list.append(user_input)

for j in range (1,len(list)):
    key = list[j]
    k=j-1
    while(k>=0 and list[k]>key):
        list[k+1]=list[k]
        k=k-1

    list[k+1]=key

print ("Sorted list:",list)
