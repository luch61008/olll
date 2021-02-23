import olll

reduced_basis = olll.reduction([
   [1,0,0,1,1,0,1],
   [0,1,0,5,0,0,0],
   [0,0,1,0,5,0,5],
],0.75)

print(reduced_basis)
