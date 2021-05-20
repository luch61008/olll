import olll
import numpy as np
import random

n = 8
k = 5
p = 1
r = 2
id = np.identity(k)

A = [[]] * k
B = [[]] * r
Z = [[]] * (k-r)

# generate a random basis
for i in range (r):
    B[i] = random.sample(range(-5,5),n)
    
# generate k random linearly combinations
for i in range (k-r):
    z = random.sample(range(-5,5),r)
    Z[i] = z

# Compute a generating set
for i in range (k-r):
    #print("z=",z,type(z))
    x = list(np.matmul(Z[i],B))
    #print(x)
    A[i] = x
for i in range (k-r, k, 1):
    A[i] = B[i-(k-r)]

print("Basis = ", B, type(B))
print("Z = ", Z, type(Z))
print("A = ", A, type(A))

A = [[-20,18,-14,24,6,-6,32,32],[-5,1,0,4,6,2,6,6],[-20,32,-28,32,-12,-20,40,40],[5,-1,0,-4,-6,-2,-6,-6],[0,-7,7,-4,9,7,-4,-4]]
print("A=",A,type(A))

A1 = [[]] * k
for i in range(k):
    a = A[i]
    a = [j * (2**p) for j in a]
    t = [int(j) for j in id[i]]+a
    A1[i]=t
print(A1,type(A1))

rb = olll.reduction(A1,0.75)
print("Basis:", rb)