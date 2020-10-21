n=int(input())
a=bin(n).replace("0b", "")
count=0
count_max=[]
for i in str(a):
    
    if i=='1':
        count+=1
    elif i=='0':
        count=0
        pass
    count_max.append(count)
print(max(count_max))

    
