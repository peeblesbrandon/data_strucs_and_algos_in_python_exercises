from colorama import Fore, Back, Style

class Empty(Exception):
    pass 

class doubleEndedQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * doubleEndedQueue.DEFAULT_CAPACITY 
        self._size = 0
        self._front = 0 
        print(Fore.YELLOW, "__init__:\t", Style.RESET_ALL, self._data)

    def __len__(self):
        return self._size 

    def is_empty(self): 
        return self._size == 0

    def add_first(self, e): 
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        if self._size != 0:
            # decrement front
            self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e # set value of front to e
        self._size += 1
        print(Fore.YELLOW, "Add first:\t", Style.RESET_ALL, self._data)

    def add_last(self, e): 
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        print(Fore.YELLOW, "Add last:\t", Style.RESET_ALL, self._data)
    
    def delete_first(self):
        if self._size == 0:
            raise Empty('queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None 
        self._front = (self._front + 1) % len(self._data)  # increment front
        self._size -= 1
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        print(Fore.YELLOW, "Delete first:\t", Style.RESET_ALL, self._data)
        return answer

    
    def delete_last(self):
        if self._size == 0:
            raise Empty('queue is empty')
        last = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last]
        self._data[last] = None
        self._size -= 1
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        print(Fore.YELLOW, "Delete last:\t", Style.RESET_ALL, self._data)
        return answer
    
    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def _resize(self, cap):
        old = self._data 
        self._data =  [None] * cap 
        step = self._front 
        for k in range(self._size):   
            self._data[k] = old[step]
            step = (step + 1) % len(old)
        self._front = 0
        print(Fore.YELLOW, "Resize:\t", Style.RESET_ALL, self._data)



if __name__ == '__main__':
    q = doubleEndedQueue()
    q.add_first(0)
    assert q.first() == 0, "First element should be: 0"
    for i in range(1, 9):
        q.add_last(i)
    for i in range(4):
        q.delete_first()
    for i in range(9, 12):
        q.add_last(i)
    assert q.last() == 11, "Last element should be: 11"
    for i in range(3, -1, -1):
        q.add_first(i)
    assert len(q._data) == 20, "Length of underlying array should have doubled to 20"
    assert q.last() == 11, "Last element should be: 11"
    assert q.is_empty() == False, "is_empty should return false"
    for i in range(9):
        q.delete_first()
    assert len(q._data) < 20, "Underlying array should've been resized to reduce space used"
