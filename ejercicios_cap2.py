import numpy as np
'''
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
'''
############################################################################
#Merge sort
#A=[35,18,22,45,39,2]
#A=np.asarray(A)

def mergeSort(Array):
    if len(Array)>1:
        n=len(Array)
        q=len(Array)//2
        L=Array[:q]
        R=Array[q:]

        mergeSort(L)
        mergeSort(R)

        print(L)
        print(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if (L[i]<R[j]):
                Array[k]=L[i]
                i=i+1
            else:
                Array[k]=R[j]
                j=j+1
            k=k+1

        while i<len(L):
            Array[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            Array[k]=R[j]
            j=j+1
            k=k+1

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





#vamos a construir los arrays L[1..n1+1] y R[1,..,n2+1]
