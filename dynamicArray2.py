# unguided implementation of a mutable array 
# with automatic resizing and other standard methods
import ctypes, os

class DynamicArray():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._Array = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, index):
        if 0 <= index < self._n:
            return self._Array[index]
        else: 
            raise ValueError("invalid index")

    def _resize(self, capacity):
        B = self._make_array(capacity)
        for i in range(self._n):
            B[i] = self._Array[i]
        self._Array = B
        self._capacity = capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, item):
        if self._n == self._capacity: 
            self._resize(2 * self._capacity)
        self._Array[self._n] = item
        self._n += 1
        
    def insert(self, index, item):
        if not 0 <= index <= self._n: 
            raise ValueError("invalid index")
        if self._n == self._capacity:
            self._resize(2 *  self._capacity)
        for j in range(self._n, j, -1):
            self._Array[j] = self[j - 1]
        self._Array[j] = item
        self._n += 1

    def remove(self, item):
        # search for item in list
        for i in range(self._n):
            if self._Array[i] == item:
                removed_index = i
        # shift elements left
        for j in range(self._n - 1, removed_index, -1):
            self._Array[j - 1] = self._Array[j]

        # resize if capacity utilization <= 25%
        if self._n / self._capacity <= 0.25:
            self._resize(self._capacity // 2)
        
        # update count of items in list
        self._n -= 1
        
        return removed_index

    def pop(self, index = None):
        # check if index was given, else remove last one
        if index == None:
            index = self._n - 1
        
        # error checking on index
        if not 0 <= index < self._n:
            raise ValueError("invalid index")
        
        # archive item and remove it
        item_removed = self._Array[index] 
        self._Array[index] = None

        # shift array elements if needed 
        for j in range(self._n - 1, index, -1):
            self._Array[j - 1] = self._Array[j]

        # resize if capacity utilization <= 25%
        if self._n / self._capacity <= 0.25:
            self._resize(self._capacity // 2)

        # update count of items in list
        self._n -= 1

        return item_removed
    
    def capacity(self):
        return int(self._capacity)


if __name__ == '__main__':
    list = DynamicArray()
    print("Initial items in list:", len(list))
    print("Appending some items...")
    list.append(2)
    list.append(5)
    for i in range(len(list)):
        print("The value at index {0} is: {1}".format(i, list[i]))
    print("Adding some more values and reprinting...")
    list.append(4)
    list.append(7)
    for i in range(len(list)):
        print("The value at index {0} is: {1}".format(i, list[i]))
    print("Popping off last value")
    print("Removed value was: {0}".format(list.pop()))
    for i in range(len(list)):
        print("The value at index {0} is: {1}".format(i, list[i]))
    print("Removing 5 from list...")
    list.remove(5)
    for i in range(len(list)):
        print("The value at index {0} is: {1}".format(i, list[i]))
    for i in range(10):
        list.append(i)
        print("Appending {0}... now the capacity is {1}".format(i, list.capacity()))
    for i in range(10):
        list.pop()
        print("Popping last element... now the capacity is {0}".format(list.capacity()))