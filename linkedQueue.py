class LinkedQueue:
    #private node class for use in linkedqueue class
    class _Node:
        __slots__ = '_element', '_next'  # for more streamlined space usage
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):    
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, e):    # enqueue to tail of queue (create node and assign to next value of tail, then map tail to it)
        if self.is_empty():
            self._head = self._Node(e, None)
            self._tail = self._head
        else:
            self._tail._next = self._Node(e, None)
            self._tail = self._tail._next
        self._size += 1

    def dequeue(self):   # dequeue from head of queue (no way to easily remove from tail of queue)
        if self.is_empty():
            raise Empty('queue is empty')
        elem = self._head._element 
        self._head = self._head._next 
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return elem

    def top(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._head._element

    def bottom(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._tail._element


# helper class for handling empty error
class Empty(Exception):
    pass


if __name__ == '__main__':
    print("...running tests")
    q = LinkedQueue()
    assert q.is_empty() == True, "Queue should start out empty"
    q.enqueue(0)
    assert q.top() == q.bottom(), "After adding one element, head and tail should match"
    for i in range(1,5):
        q.enqueue(i)
    assert len(q) == 5, "length of queue should now equal 5"
    assert q.dequeue() == 0, "Dequeing should return the element added first from head of queue: 0"
    print("All tests passed!")
