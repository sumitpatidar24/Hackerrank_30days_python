t=int(input())

s=[str(input()) for x in range(t)]

for i in s:
    e=""
    o=""
    for j in range(len(str(i))):
        if j%2==0:
            e+=i[j]
        else:
            o+=i[j]
    print(e,o)
