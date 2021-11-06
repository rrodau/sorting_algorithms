class Heap:

    def __init__(self, heap_type=int) -> None:
        self.heap_list = []
        self.count = 0
        self.heap_type = heap_type

    def parent_idx(self, idx: int):
        """ 
        A function that returns the parent index of an element

        @params:
            idx -> Index of element which parent needs to be found 

        @return:
            the index of the elements parent
        """
        return idx // 2

    def left_child_idx(self, idx: int) -> int:
        """
        A function that returns the left child index of an element

        @params:
            idx -> Index of element which left child needs to be found

        @return:
            the index of the elements left child
        """
        return idx * 2 + 1

    def right_child_idx(self, idx: int) -> int:
        """
        A function that returns the right child index of an element

        @params:
            idx -> Index of element which right child needs to be found

        @return:
            the index of the elements right child
        """
        return idx * 2 + 2

    def get_larger_child(self, idx: int) -> int:
        """
        A function that return the index of the child element which is larger

        @params:
            idx -> The parent index

        @return:
            the index of the larger child
        """
        right_child_idx = self.right_child_idx(idx)
        left_child_idx = self.left_child_idx(idx)
        # if does not have a right child, there is only a left child
        if right_child_idx > self.count - 1:
            return left_child_idx
        # if left child is larger than right child
        elif self.heap_list[left_child_idx] > self.heap_list[right_child_idx]:
            return left_child_idx
        # if right child is larger than left child
        else:
            return right_child_idx


    def child_present(self, idx) -> bool:
        """
        A function that returns True if the element has a child

        @params:
            idx -> index of parent

        @return:
            True if child exists False otherwise
        """
        return self.left_child_idx(idx) <= self.count - 1 
    
    def add(self, element) -> None:
        """
        A function that add an element to the heap

        @params:
            element -> An element of the heap_type that needs to be added to the heap
        
        @return:
            None
        """
        if isinstance(element, self.heap_type):
            self.count += 1
            self.heap_list.append(element)
            self.heapify_up()
        else:
            raise ValueError(f"Expected {self.heap_type} but got {type(element)}")
    
    def retrive_max(self):
        """
        A function that returns the root element and sets the last element to be the root element and then
        restores the heap property
        """
        # if heap is empty
        if self.count == 0:
            return None
        max_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()
        self.count -= 1
        self.heapify_down()
        return max_val


    def heapify_up(self) -> None:
        """
        A function that restores the heap property bottom-up (that the children are smaller than the parent)
        """ 
        # start at the last element of the list
        idx = self.count - 1
        # while there's a parent element available
        while self.parent_idx(idx) >= 0:
            child = self.heap_list[idx]
            parent_idx = self.parent_idx(idx)
            parent = self.heap_list[parent_idx]
            # check if parent is smaller than child if so, swap them
            if parent < child:
                self.heap_list[parent_idx] = child
            if parent_idx == 0:
                break
            idx = parent_idx

    def heapify_down(self) -> None:
        """
        A function that restores the heap property top-down
        """
        idx = 0
        # while there is a children
        while self.child_present(idx):
            #print(idx)
            # get the lareger childern
            larger_children_idx = self.get_larger_child(idx)
            child = self.heap_list[larger_children_idx]
            parent = self.heap_list[idx]
            # if child element is greater than parent element than thex need to be swapped
            if child > parent:
                self.heap_list[idx] = child
                self.heap_list[larger_children_idx] = parent
            idx = larger_children_idx


