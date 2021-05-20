import olll
import numpy as np
import random

n = 8
k = 5
p = 2
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

#print("Basis = ", B, type(B))
#print("Z = ", Z, type(Z))
#print("A = ", A, type(A))

#A = [[-20,18,-14,24,6,-6,32,32],[-5,1,0,4,6,2,6,6],[-20,32,-28,32,-12,-20,40,40],[5,-1,0,-4,-6,-2,-6,-6],[0,-7,7,-4,9,7,-4,-4]]
#print("A=",A,type(A))

A1 = [[]] * k
for i in range(k):
    a = A[i]
    a = [j * (2**p) for j in a]
    t = [int(j) for j in id[i]]+a
    A1[i]=t

A2 = [[1 for j in range(n+k)] for i in range(k)]
for i in range (k):
    for j in range(n+k):
        A2[i][j] = A1[i][j]

print("\n\nA1 = ", A1)
print("\n\nA2 = ", A2)
#A1 = [[1, 0, 0, 0, 0, 0, 2, -36, 28, -10, -38, -16, 30], [0, 1, 0, 0, 0, 0, 58, 0, -16, -38, 14, 4, 6], [0, 0, 1, 0, 0, 0, 12, 16, -16, -4, 20, 8, -12], [0, 0, 0, 1, 0, 0, -6, -8, 8, 2, -10, -4, 6], [0, 0, 0, 0, 1, 0, -10, 6, -2, 8, 4, 2, -6]]
#A1 = [[1, 0, 0, 0, 0, 24, -44, 24, -32, -12, 8, 20, -16], [0, 1, 0, 0, 0, 36, -92, 84, -68, -24, 8, 44, -40], [0, 0, 1, 0, 0, 24, -44, 24, -32, -12, 8, 20, -16], [0, 0, 0, 1, 0, -16, 12, 16, 8, 4, -8, -4, 0], [0, 0, 0, 0, 1, -4, 16, -20, 12, 4, 0, -8, 8]]


rb = olll.reduction(A2,0.75)
print("\n\n Original Basis = ", B)
print("\n\n A = ", A)
print("\n\n Reduced Basis = ", rb)
