import numpy as np

def insertionSort(Array):
    for j in range(0,len(Array)):
        key=Array[j]
        i=j-1
        while (i>=0) and (Array[i]>key):
            Array[i+1]=Array[i]
            i=i-1
        Array[i+1]=key

def mergeSort(Array):
    if len(Array)>1:
        n=len(Array)
        q=len(Array)//2
        L=Array[:q]
        R=Array[q:]
        if len(L)>4:
            mergeSort(L)
            mergeSort(R)
        else:
            #vamos a utilizar isertionSort para inputs pequeños
            insertionSort(L)
            insertionSort(R)
            print('se utilizó isertion sort')

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
    array = [6, 5, 12, 10, 9, 1,45,33,65,14,32,55,86,102,2,12,44,59]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
