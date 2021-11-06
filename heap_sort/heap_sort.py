from heap import *

def heapsort(lst):
    sorted_lst = []
    heap = Heap()
    for el in lst:
        heap.add(el)
    # while there are elements in heap
    while heap.count > 1:
        max_value = heap.retrive_max()
        sorted_lst.insert(0, max_value)
    return sorted_lst


my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
# print the sorted list
print(sorted_list)