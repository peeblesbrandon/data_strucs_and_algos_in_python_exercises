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

    def insert(self, index, e):
        # check for errors
        if index < 0:
            raise IndexError('Index must be a non-negative integer')
        if index > (self._size):
            raise IndexError('Index cannot be greater than length of existing list')
        
        # insert the item 
        if self.is_empty():                                 # if empty
            self._head = self._Node(e, None)
            self._tail = self._head 
        elif index == 0:                                    # append to front 
            self._head = self._Node(e, self._head)
        elif index == self._size:                           # append to end 
            self._tail._next = self._Node(e, None)
            self._tail = self._tail._next 
        else:                                               # insert elsewhere in list
            i = 1
            prev = self._head
            curr = prev._next 
            while i < index: 
                prev = curr
                curr = curr._next
                i += 1
            prev._next = self._Node(e, curr) 
        
        # increment size 
        self._size += 1


    def reverse(self):
        # iterators 
        prev = None 
        curr = self._head
        next = None
        # iterate through linked list
        while curr:
            next = curr._next 
            curr._next = prev 
            prev = curr 
            curr = next 
        # swap head and tail 
        self._head, self._tail = self._tail, self._head

    def value_at(self, index):
        # check for errors
        if index < 0:
            raise IndexError('Index must be a non-negative integer')
        if index > (self._size - 1):
            raise IndexError('Index outside of range')
        # iterate through list
        i = 0
        curr = self._head 
        while i != index:
            curr = curr._next 
            i += 1 
        return curr._element

    def remove(self, e):
        curr = self._head 
        next = curr._next 
        if e == self._head._element:
            self._head = next 
            curr = None 
        else:
            while next and next._element != e:
                curr = next 
                next = curr._next 
            if not next:
                raise ValueError('value not found in list')
            curr._next = next._next 
            if next == self._tail:
                self._tail = curr
            next = None 
        self._size -= 1



    def print(self):
        print('Elements in queue: ', end='')
        curr = self._head
        while curr:
            print(curr._element, end='')
            curr = curr._next
            if curr:
                print(', ', end='')
            else:
                print('')


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
    q.print()
    q.reverse()
    q.print()
    q.insert(1, 8)
    q.print()
    q.insert(0, 9)
    q.print()
    q.insert(len(q), 8)
    q.print()
    assert q.value_at(0) == 9, "0th value should be 9"
    assert q.value_at(3) == 3, "value at index 3 should be 3"
    assert q.value_at(len(q) - 1) == 8, "value at end of list should be 8"
    q.remove(3)
    q.print()
    q.remove(9)
    q.print()
    q.remove(8)
    q.print()
    q.remove(8)
    q.print()
    assert q.bottom() == 1, "tail should equal 1"
    print("All tests passed!")
