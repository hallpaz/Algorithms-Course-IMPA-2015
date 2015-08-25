

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

def insertion_sort(array: list)->list:
    """ This function implements the insertion sort method"""

    for i in range(1, len(array)):
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

def quicksort(array: list)->list:
    pass

def heapsort(array: list)->list:
    pass


if __name__ == "__main__":
    print("Sorting file called as main script")
