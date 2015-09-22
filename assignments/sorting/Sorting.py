import random

def selection_sort(array: list)->list:
    """This function implements the selection sort method"""

    for i in range(len(array)-1):
        min_index = i
        for j in range(i, len(array)-1):
            if(array[j] < array[min_index]):
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return

def insertion_sort(array: list, start = None, end = None)->list:
    """ This function implements the insertion sort method"""
    start = start or 1
    if(end is None):
        end = len(array)
    for i in range(start, end):
        current_value = array[i]
        j = i-1
        while(current_value < array[j] and j >= 0):
            array[j+1] = array[j]
            j-=1
        array[j+1] = current_value

    return

def merge(array: list, start: int, middle: int, end: int):
    left = array[start:middle+1] #python excludes the last
    right = array[middle+1:end+1]

    i, j = 0, 0
    k = start
    while(k < end+1):
        if(left[i] < right[j]):
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        if(i >= len(left)): #left is over
            while(j < len(right)):
                k+=1
                array[k] = right[j]
                j+=1
        elif(j >= len(right)):
            while(i < len(left)):
                k+=1
                array[k] = left[i]
                i+=1
        k+=1
    return

def mergesort(array: list, start= 0, end= None):
    """ This function implements the merge sort algorithm """
    if(end is None): #can't rely on None, because 0 is equal to false
        end = len(array)-1

    if(start < end):
        middle = (start + end)//2
        mergesort(array, start, middle)
        mergesort(array, middle+1, end)
        merge(array, start, middle, end)

    return


def partition(array, start, end):
    i = start
    for j in range(start + 1, end + 1):
        if array[j] < array[start]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i], array[start] = array[start], array[i]
    return i

def rdm_partition(array: list, start: int, end: int)->int:
    """Quicksort auxiliary routine"""
    k = random.randint(start, end)
    array[k], array[start] = array[start], array[k]
    return partition(array, start, end)

def quicksort(array, start=0, end=None):
    if(end is None):
        end = len(array)-1
    if end > start: # Verifica se a lista tem 2 ou mais itens
        pivotIndex = rdm_partition(array, start, end) # Pega a posicao do pivo
        quicksort(array, start, pivotIndex - 1) # Ordena recursivamente os itens menores que o pivo
        quicksort(array, pivotIndex + 1, end) # Ordena recursivamente os itens maiores que o pivo

def max_heapify(array:list, index:int, heap_size = None):
    """Makes the ith element of a list to respect the max heap property"""
    if(heap_size is None):
        heap_size = len(array)

    max_index = index
    left = 2*index+1
    if((left < heap_size) and (array[left] > array[max_index])):
        max_index = left
    right = 2*index+2
    if((right < heap_size) and (array[right] > array[max_index])):
        max_index = right
    if(max_index != index):
        aux_bucket = array[index]
        array[index] = array[max_index]
        array[max_index] = aux_bucket

        max_heapify(array, max_index, heap_size)

    return

def validate_heap(array:list, heap_size=-1)->str:
    if(heap_size is None):
        heap_size = len(array)

    for i in range(heap_size//2):
        left = 2*i+1
        right = 2*i+2
        if(left < heap_size and array[i] < array[2*i+1]):
            print("HEAP PROPERTY VIOLATION", heap_size, array)
            break
        if(right < heap_size and array[i] < array[2*i+2]):
            print("HEAP PROPERTY VIOLATION", heap_size, array)
            break
    return "HEAP IS OK"

def build_heap(array:list):
    """Builds a heap of maximum from a list"""

    for i in range(len(array)//2, -1, -1):
        max_heapify(array, i)

def heapsort(array: list)->list:
    """Heapsort algorithm"""

    build_heap(array)
    i = len(array)

    while(i > 0):
        i-=1
        aux_bucket = array[i]
        array[i] = array[0]
        array[0] = aux_bucket
        max_heapify(array, 0, i)
    return

def adaptative_mergesort(array: list, start=0, end = None, threshold = 10):
    """This function uses the mergesort algorithm to sort large arrays and
    transitions to the insertion sort algorithm when the problem size is less
    then or equal to a given threshold"""

    if(end is None):
        end = len(array)-1

    if(start < end):
        middle = (start + end)//2
        if(middle - start + 1 < threshold):
            insertion_sort(array, start, middle+1)
            insertion_sort(array, middle+1, end+1)
        else:
            adaptative_mergesort(array, start, middle)
            adaptative_mergesort(array, middle+1, end)
        merge(array, start, middle, end)

    return

def adaptative_quicksort(array: list, start = 0, end = None, threshold = 10):
    """This function uses the quicksort algorithm to sort large arrays and
    transitions to the insertion sort algorithm when the problem size is less
    then or equal to a given threshold"""

    if(end is None):
        end = len(array)-1

    if end - start > threshold:
        pivotIndex = rdm_partition(array, start, end)
        adaptative_quicksort(array, start, pivotIndex - 1)
        adaptative_quicksort(array, pivotIndex + 1, end)
    else:
        insertion_sort(array, start, end+1)
    return

def adaptative_quicksort_v2(array: list, start = 0, end = None, threshold = 10):
    """This function uses the quicksort algorithm to sort large arrays and
    transitions to the insertion sort algorithm when the problem size is less
    then or equal to a given threshold"""

    if(end is None):
        end = len(array)-1

    if start < end:
        pivotIndex = partition(array, start, end)
        if(end-start+1 < threshold):
            insertion_sort(array, start, pivotIndex+1)
            insertion_sort(array, pivotIndex+1, end+1)
        else:
            adaptative_quicksort(array, start, pivotIndex - 1)
            adaptative_quicksort(array, pivotIndex + 1, end)

    return


def tco_quicksort(array: list, start = 0, end = None):
    """Quicksort algorithm with Tail Call Optimization to avoid stack overflow"""

    if(end is None):
        end = len(array)-1

    while(start < end):
        point = partition(array, start, end)
        if (point - start < end - point):
            tco_quicksort(array, start, point-1)
            start = point+1
        else:
            tco_quicksort(array, point+1, end)
            end = point-1

if __name__ == "__main__":
    print("Sorting file called as main script")
