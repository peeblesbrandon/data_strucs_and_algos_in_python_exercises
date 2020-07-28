import sys

class MinHeap:
    def __init__(self, contents=()): 
        self.heap = [ j for element in contents ] # will be empty unless list provided
        if len(self.heap) > 0:
            self.min_heapify() # will construct heap with provided contents if theyre provided

    def __len__(self):
        return len(self.heap)

    # let j equal the position of an element 
    def parent(self, j): 
        return (j - 1) // 2 
    
    def left(self, j):
        return 2*j + 1 

    def right(self, j):
        return 2*j + 2 
    
    def has_left(self, j): 
        return self.left(j) < len(self.heap)    # returns false if index of left child would be beyond current len 

    def has_right(self, j): 
        return self.right(j) < len(self.heap)   # similar to has_left

    # let i equal position of another element (parent or child)
    def swap(self, i, j): 
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def upheap(self, j):
        parent = self.parent(j) # get the parents position
        if j > 0 and self.heap[j] < self.heap[parent]:
            self.swap(parent, j)
            self.upheap(parent)
        # terminates if j was the root or if it already satisfies heap-order property

    # def downheap(self, j):

    # def insert(self, element):
    
    # def remove_min(self): 

    # def min(self):

    # def min_heapify(self):


    
if __name__ == '__main__':
    myHeap = MinHeap()
    print('Heap initialized to length of ' + str(len(myHeap)))
