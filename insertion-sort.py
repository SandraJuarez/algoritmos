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

#searching problem

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
