import sys
n=int(input())
dict={}
for i in range(n):
    a=list(map(str,input().split()))
    name=str(a[0])
    no=int(a[1])
    dict[name]=no



try:
    while True:
        bb=input()
        if bb in dict.keys():
            print("{}={}".format(bb,dict[bb]))
            
        else:
            print("Not found")
        
except(EOFError):
    pass

