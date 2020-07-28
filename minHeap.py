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
    
    # def has_left(self, j): 

    # def has_right(self, j): 

    # # let i equal position of another element (parent or child)
    # def swap(self, i, j): 
        
    # def upheap(self, j):

    # def downheap(self, j):

    # def insert(self, element):
    
    # def remove_min(self): 

    # def min(self):

    # def min_heapify(self):


    
if __name__ == '__main__':
    myHeap = MinHeap()
    print('Heap initialized to length of ' + str(len(myHeap)))