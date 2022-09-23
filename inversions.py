#sea A[1,..n] un array de n numeros. Si i<j y A[i]>A[j] el par i j es ua inversiónote
#Se realiza un algoritmo que deterina el número de inversiones en cualquier arrays

def mergeSort(Array):

    if len(Array)>1:
        n=len(Array)
        q=int(round(len(Array)/2))
        L=Array[:q]
        R=Array[q:]
        global contador_inversiones
        contador_inversiones=0
        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if (L[i]<R[j]):
                Array[k]=L[i]
                i=i+1
            else:
                Array[k]=R[j]
                j=j+1
                print("la matriz izquierda fue mayor")
                contador_inversiones=contador_inversiones+q-i
            k=k+1

        while i<len(L):
            Array[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            Array[k]=R[j]
            j=j+1
            k=k+1
    return contador_inversiones

# Print the array



# Driver program
if __name__ == '__main__':
    array = [2, 3, 8, 6, 1]

    contador=mergeSort(array)
    print(contador)
