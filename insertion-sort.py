import numpy as np

A=(61,41,59,26,41,58)
A=np.asarray(A)
print(A)
print(len(A))

#ordena A en forma descendente
#key=np.zeros((len(A)))
for j in range(1,len(A)):
    key=A[j]
    i=j-1
    while (i>=0) and (A[i]>key):
        A[i+1]=A[i]
        i=i-1
    A[i+1]=key

print('A ordenado descendiente es:',A)



#ahora vamos a ordenar en forma descendiente
A=(31,41,59,26,41,58)
A=np.asarray(A)
for j in range(0,len(A)):
    key=A[j]
    i=j-1
    while (i>=0) and (A[i]<key):
        A[i+1]=A[i]
        i=i-1
    A[i+1]=key

print('A ordenado ascendente es:',A)
