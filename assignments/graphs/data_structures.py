
#A min priority-queue
class Priority_Queue():
    def __init__(self, array = []):
        self.storage = array
        self.size = len(self.storage)
        build_heap(array)


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

    def build_heap(self, array:list):
        """Builds a heap of maximum from a list"""

        for i in range(len(array)//2, -1, -1):
            max_heapify(array, i)
