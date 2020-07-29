import sys
class Empty(Exception):
    pass

class MinHeap:
    def __init__(self, contents=()): 
        self.heap = [ j for element in contents ] # will be empty unless list provided
        if len(self.heap) > 0:
            self.min_heapify() # will construct heap with provided contents if theyre provided

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    # let j equal the position of an element 
    def parent(self, j): 
        return (j - 1) // 2 
    
    def left(self, j):
        return 2*j + 1 

    def right(self, j):
        return 2*j + 2 
    
    def has_left(self, j): 
        return self.left(j) < len(self)    # returns false if index of left child would be beyond current len 

    def has_right(self, j): 
        return self.right(j) < len(self)   # similar to has_left

    # let i equal position of another element (parent or child)
    def swap(self, i, j): 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def upheap(self, j):
        parent = self.parent(j) # get the parents position
        if j > 0 and self.heap[j] < self.heap[parent]:
            self.swap(parent, j)
            self.upheap(parent)
        # terminates if j was the root or if it already satisfies heap-order property

    def downheap(self, j):
        if self.has_left(j):  # terminates if no left child (meaning its a leaf or empty)
            left = self.left(j)
            smallest_child = left  # even though it might not yet be proven to be smallest
            if self.has_right(j):
                right = self.right(j)
                if self.heap[right] < self.heap[smallest_child]:
                    smallest_child = right
            if self.heap[j] > self.heap[smallest_child]:
                self.swap(j, smallest_child)
                self.downheap(smallest_child)

    def insert(self, element):
        self.heap.append(element)
        self.upheap(len(self) - 1)
    
    def remove_min(self): # return the removed value
        min = self.min() # store min val if exists
        self.swap(0, len(self) - 1) # swap min with last element
        self.heap.pop() # remove last element (min)
        self.downheap(0) # bubble down the moved value to correct heap
        return min 

    def min(self):
        if self.is_empty():
            raise Empty("Heap is empty")
        return self.heap[0]

    def min_heapify(self):
        start = self.parent(len(self) - 1)
        for j in range(start, -1, -1):
            self.downheap(j)


    
if __name__ == '__main__':
    myHeap = MinHeap()
    print('Heap initialized to length of ' + str(len(myHeap)))
    myHeap.insert(3)
    myHeap.insert(1)
    myHeap.insert(5)
    myHeap.insert(2)
    print('Parent of ' + str(myHeap.heap[3]) + ' is at position ' + str(myHeap.parent(3)))
    print(myHeap.heap)
    print('Removing minimum which is ' + str(myHeap.remove_min()))
    print(myHeap.heap)
    for i in range(1000000):
        myHeap.insert(i)

