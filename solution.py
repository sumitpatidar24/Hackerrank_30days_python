arr=[]
for i in range(6):
    a=[int(x) for x in input().split()]
    arr.append(a)
def func_of_sum(mat,row,col):
    sums=0
    sums+=mat[row-1][col-1]
    sums+=mat[row-1][col]
    sums+=mat[row-1][col+1]
    sums+=mat[row][col]
    sums+=mat[row+1][col-1]
    sums+=mat[row+1][col]
    sums+=mat[row+1][col+1]
    return sums
sum_list=[]

for x in range(1,5):
    for y in range(1,5):
        summing=func_of_sum(arr,x,y)
        sum_list.append(summing)
            
print(max(sum_list))
