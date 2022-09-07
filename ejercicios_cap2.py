import numpy as np

A=(35,18,22,45,39,2)

A=np.asarray(A)

#selection sort
for i in range(0,len(A)):
    j=i+1
    while j<len(A):
        if(A[i]>A[j]):
            save=A[i]
            A[i]=A[j]
            A[j]=save
            j=j+1
        else:
            j=j+1
        print(A)
