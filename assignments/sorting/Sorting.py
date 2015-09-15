

def selection_sort(array: list)->list:
    """This function implements the selection sort method"""

    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if(array[j] < array[min_index]):
                min_index = j
        exch_bucket = array[i]
        array[i] = array[min_index]
        array[min_index] = exch_bucket

    return array

def insertion_sort(array: list, start = None, end = None)->list:
    """ This function implements the insertion sort method"""
    start = start or 1
    end = end or len(array)
    for i in range(start, end):
        current_value = array[i]
        j = i-1
        while(current_value < array[j] and j >= 0):
            array[j+1] = array[j--]
        array[j+1] = current_value

    return array

def merge(array: list, start: int, middle: int, end: int):
    left = []
    right = []
    for i in range(start, middle):
        left[i-start] = array[i]
    for i in range(middle, end):
        right[i-middle] = array[i]

    i, j = 0, 0
    for k in range(start, end):
        if(left[i] < right[i]):
            array[k] = left[i++]
        else:
            array[k] = right[j++]
        if(i >= len(left)):
            while(j < len(right)):
                array[k++] = right[j++]
        elif(j >= len(right)):
            while(i < len(left)):
                array[k++] = left[i++]
    return

def mergesort(array: list, start: int, end: int):
    """ This function implements the merge sort algorithm """

    if(start < end):
        middle = (start + end)//2
        mergesort(array, start, middle)
        mergesort(array, middle, end)
        merge(array, start, middle, end)

    return

def partition(array: list, start: int, end: int)->int:
    """Quicksort auxiliary routine"""

    pivot_value = array[end]
    i = 0
    for j in range(start, end):
        if(array[j] <= pivot_value):
            aux = array[i]
            array[i] = array[j]
            array[j] = array[i]
            i += 1
    array[end] = array[i]
    array[i] = pivot_value
    return i

def quicksort(array: list, start = 0, end = None):
    """Quicksort algorithm"""

    end = end or len(array)-1

    if(start < end):
        point = partition(array, start, end)
        quicksort(array, start, point)
        quicksort(array, point, end)

def heapsort(array: list)->list:
    """Heapsort algorith"""

    pass


def adaptative_mergesort(array: list, start:int, end:int, threshold = 10):
    """This function uses the mergesort algorithm to sort large arrays and
    transitions to the insertion sort algorithm when the problem size is less
    then or equal to a given threshold"""

    if(start < end):
        if((end-start +1) <= threshold):
            insertion_sort(array, start, end)
        else:
            middle = (start + end)//2
            adaptative_mergesort(array, start, middle)
            adaptative_mergesort(array, middle, end)
            merge(array, start, middle, end)
    return

def adaptative_quicksort(array: list, start = 0, end = None, threshold = 10):
    """This function uses the quicksort algorithm to sort large arrays and
    transitions to the insertion sort algorithm when the problem size is less
    then or equal to a given threshold"""

    end = end or len(array)-1

    if(start < end):
        if((end-start+1) < threshold):
            insertion_sort(array, start, end)
        else:
            point = partition(array, start, end)
            adaptative_quicksort(array, start, point)
            adaptative_quicksort(array, point, end)
    return


if __name__ == "__main__":
    print("Sorting file called as main script")
