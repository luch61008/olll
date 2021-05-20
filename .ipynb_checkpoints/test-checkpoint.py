import olll
import numpy as np

test1 = [[1,0,0,1,1,0,1],[0,1,0,5,0,0,0],[0,0,1,0,5,0,5]]
test2 = [[1,0,0,2,-1,1],[0,1,0,3,-4,-2],[0,0,1,5,-10,-8]]
test3 = [[1,0,0,1,1,0,1], [0,1,0,4,-1,0,-1], [0,0,1,1,1,0,1]]
test4 = [[1,0,0,2,5,3],[0,1,0,1,1,1,],[0,0,1,4,-2,0]]
test5 = [[1,0,0,0,0,0,2,1,1,2],[0,1,0,0,0,0,1,1,-1,-1],[0,0,1,0,0,0,-1,0,-2,-3],[0,0,0,1,0,0,1,-1,1,-1],[0,0,0,0,1,0,-1,2,-4,-3],[0,0,0,0,0,1,1,0,0,1]]
test6 = [[1, 0, 0, 5, 0, 0, 0],[0, 1, 0, 0, 5, 0, 5],[0, 0, 1, 1, 1, 0, 1]]
test7 = [[1, 0, 0, 20, 0, 0, 0],[0, 1, 0, 0, 20, 0, 20],[0, 0, 1, 4, 4, 0, 4]]
test8 = [[1, 0, 0, 10, 0, 0, 0],[0, 1, 0, 0, 10, 0, 10],[0, 0, 1, 2, 2, 0, 2]]


n = input("Please enter n: \n")
n = int(n)
k = input("Please enter k: \n")
k = int(k)
p = input("Please enter p: \n")
p = int(p)

id = np.identity(k)

A = [[]] * k
print("Please enter the generating set:\n")
for i in range(k):
    print("\nEnter the generator a[",i,"]: ")
    a = list(map(int,input().strip().split()))[:n]
    #print(i, a)
    a = [x * (2**p) for x in a]
    
    y = list(id[i])
    print(y[i],type(y[i]))
    A[i] = y+a
    print(A[i], type(A[i]))
print(A, type(A))
print(test7, type(test7))
rb = olll.reduction(test7,0.75)
print("Basis: ", rb)
