class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element 
            self._next = next 
    
    def __init__(self):
        self._head = None 
        self._size = 0  

    def is_empty(self):
        return self._size == 0 
    
    def __len__(self):
        return self._size
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        poppedElem = self._head._element
        self._head = self._head._next
        self._size -= 1 
        return poppedElem

# helper class for empty stack errors
class Empty(Exception):
    pass 


if __name__ == '__main__':
    print("...running tests")
    ls = LinkedStack()
    assert ls.is_empty() == True, "Stack should begin as empty"
    ls.push(1)
    assert ls.top() == 1, "Top (following .push(1)) should return 1"
    ls.push(2)
    assert ls.pop() == 2, "Popped element should be 2 (following .push(2))"
    for i in range(4):
        ls.push(i)
    assert len(ls) == 5, "Length should be 5 after four pushes"
    print("All tests passed!")
