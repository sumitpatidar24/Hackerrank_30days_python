n=int(input())
a=[int(x) for x in input().split()]
b=a[::-1]
for i in b:
    print(i,end=" ")
