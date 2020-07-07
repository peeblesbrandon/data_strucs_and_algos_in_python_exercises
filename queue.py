from colorama import Fore, Back, Style

class Empty(Exception):
    pass

class ArrayQueue: 
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY # use Class.global_var to access
        self._size = 0  # elements in queue
        self._front = 0 # front element in queue

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None 
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer 
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data) #get next available index to insert element
        self._data[avail] = e 
        self._size += 1 
    
    def _resize(self, cap):
        old = self._data 
        self._data = [None] * cap 
        walk = self._front 
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


# unit tests 
if __name__ == '__main__':
    print(Style.DIM, Fore.WHITE, "...running tests", Style.RESET_ALL)

    # initialization tests
    queue = ArrayQueue()
    assert isinstance(queue, ArrayQueue) == True, "Should be of class ArrayQueue"
    assert queue.is_empty() == True, "Queue should be initialized as empty"

    # enqueue and dequeue tests
    queue.enqueue(1)
    assert queue.first() == 1, "Front element should be: 1"
    for i in range(2,9):
        queue.enqueue(i)
    assert queue.dequeue() ==  1, "Dequeued element should be: 1"
    assert queue.first() == 2, "New front element should be: 2"
    queue.dequeue()
    queue.dequeue()
    for i in range(100, 103):
        queue.enqueue(i)
    assert queue._data[0] == 102, "Elements should have wrapped around -- 0th element should be: 102"
    for i in range(5):
        queue.enqueue(i)
    assert len(queue._data) == 20, "Queue should have resized to 2x default capacity"
    for i in range(10):
        queue.dequeue()
    assert len(queue._data) == 10, "Queue should reduced size by 50%"

    # print success message
    print(Fore.GREEN, "All tests passed", Style.RESET_ALL)
